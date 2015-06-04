# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystoneclient import session

from keystoneclient_kerberos.tests import base
from keystoneclient_kerberos import v3


class TestKerberosAuth(base.TestCase):

    def test_authenticate_with_kerberos_domain_scoped(self):
        token_id, token_body = self.kerberos_mock.mock_auth_success()

        a = v3.Kerberos(self.TEST_ROOT_URL + 'v3')
        s = session.Session(a)
        token = a.get_token(s)

        self.assertRequestBody()
        self.assertEqual(
            self.kerberos_mock.challenge_header,
            self.requests_mock.last_request.headers['Authorization'])
        self.assertEqual(token_id, a.auth_ref.auth_token)
        self.assertEqual(token_id, token)
