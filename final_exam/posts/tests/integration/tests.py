import pytest
from django.contrib.auth import get_user_model
from django.test import Client, RequestFactory
from django.urls import reverse

from final_exam.posts.models import Post

UserModel = get_user_model()

USER_EMAIL = "test@example.com"
USER_PASS = "test"
@pytest.fixture
def user():
    return UserModel.objects.create_user(email=USER_EMAIL, password=USER_PASS)


@pytest.fixture
def post(user):
    return Post.objects.create(author=user, title='Test Post', content='Test Content')


@pytest.fixture
def client(user):
    client = Client()
    client.force_login(user)
    return client


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.mark.django_db
class TestPostDeleteView:
    def test_successfully_deletes_post_if_user_is_author(self, client, post):
        response = client.post(reverse('post_delete', kwargs={'pk': post.pk}))
        assert response.status_code == 302
        assert Post.objects.count() == 0

    def test_returns_HttpResponseForbidden_if_user_is_not_author(self, client, post, user, request_factory):
        new_user = UserModel.objects.create_user(email='test2@abv.bg', password='test2')
        login_response = client.login(username='test2@abv.bg', password='test2')
        assert login_response is True
        response = client.post(reverse('post_delete', kwargs={'pk': post.pk}))
        assert response.status_code == 403
        assert Post.objects.count() == 1

    def test_returns_HttpResponseNotFound_if_post_does_not_exist(self, client):
        response = client.post(reverse('post_delete', kwargs={'pk': 999}))
        assert response.status_code == 404
