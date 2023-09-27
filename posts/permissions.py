from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    # 글 조회: 인증여부 관계없이 누구나
    # 글 생성: 로그인한 유저
    # 글 편집: 글 작성자
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user