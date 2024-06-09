from django.test import  Client

from projeto.django_assertions import assert_contains

def test_status_code(client:Client):
    resp = client.get(resp)
    assert resp.status_code == 200 

def test_title(resp):
   assert_contains(resp, '<title>Reizinho-imports- home</title>' )

