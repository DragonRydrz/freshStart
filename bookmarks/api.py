from rest_framework import serializers, viewsets
from .models import Bookmark, PrivateBookmark


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('name', 'address')


class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()


class PrivateBookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivateBookmark
        fields = ('name', 'address')

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        user = self.context['request'].user
        private_bookmark = PrivateBookmark.objects.create(
            user=user, **validated_data)
        return private_bookmark
        pass


class PrivateBookmarkViewset(viewsets.ModelViewSet):
    serializer_class = PrivateBookmarkSerializer
    queryset = PrivateBookmark.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PrivateBookmark.objects.none()
        else:
            return PrivateBookmark.objects.filter(user=user)
