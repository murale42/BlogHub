from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model
from blog.permissions import IsAuthorOrReadOnly, IsCommentAuthorOrReadOnly
from blog.models import Post, Category, Comment, Like, Favorite
from blog.serializers import (
    RegisterSerializer, LoginSerializer, PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer, ChangePasswordSerializer,
    AuthorSerializer, PostSerializer, CategorySerializer,
    CommentSerializer
)

User = get_user_model()

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access": access_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})

class PasswordResetRequestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user

            uid = urlsafe_base64_encode(str(user.pk).encode())
            token = default_token_generator.make_token(user)

            reset_link = f"{request.scheme}://{request.get_host()}/api/password-reset/confirm/?uidb64={uid}&token={token}"

            email_subject = "Password Reset Request"
            email_message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return Response({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostsByCategoryView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return Post.objects.filter(category__slug=category_slug)

class PostsByAuthorView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        author_username = self.kwargs['username']
        return Post.objects.filter(author__username=author_username)

class AuthorDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "username"

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommentAuthorOrReadOnly]

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked."}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, post_id):
        try:
            like = Like.objects.get(user=request.user, post_id=post_id)
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class RepostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            original_post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"message": "Original post not found."}, status=status.HTTP_404_NOT_FOUND)

        existing_repost = Post.objects.filter(author=request.user, repost_from=original_post).first()
        if existing_repost:
            return Response(
                {"message": "You have already reposted this post. Delete it first if you want to repost again."},
                status=status.HTTP_400_BAD_REQUEST
            )

        repost = Post.objects.create(
            title=f"Repost: {original_post.title}",
            content=original_post.content,
            image=original_post.image,
            video=original_post.video,
            author=request.user,
            repost_from=original_post,
            category=original_post.category
        )

        serializer = PostSerializer(repost, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UnrepostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, post_id):
        try:
            original_post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"message": "Original post not found."}, status=status.HTTP_404_NOT_FOUND)

        repost = Post.objects.filter(author=request.user, repost_from=original_post).first()
        if repost:
            repost.delete()
            return Response({"message": "Repost removed."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"message": "You have not reposted this post."}, status=status.HTTP_400_BAD_REQUEST)

class ToggleFavoritePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({"message": "Post added to favorites.", "favorited": True}, status=status.HTTP_201_CREATED)
        else:
            favorite.delete()
            return Response({"message": "Post removed from favorites.", "favorited": False}, status=status.HTTP_200_OK)
