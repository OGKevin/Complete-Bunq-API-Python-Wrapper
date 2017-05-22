from apiwrapper.endpoints.chat_conversation import ChatConversation
from tests.endpoints.test_endpoint import EndpointTest


class ChatConversationTest(EndpointTest):
    __base_endpoint_url = "/user/%d/chat-conversation"

    @property
    def _base_endpoint(self):
        return self.__base_endpoint_url % self.random_id

    def setUp(self):
        super().setUp(ChatConversation)

    def test_get_base_endpoint(self):
        endpoint_should_be = self._base_endpoint

        endpoint_to_check = self.test_class._get_base_endpoint(
            self.random_id)

        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_chat_conversations_for_user(self):
        endpoint_should_be = self._base_endpoint

        endpoint_to_check = self.test_class.get_all_chat_conversations_for_user(
            self.random_id)

        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_chat_conversation_by_id(self):
        endpoint_should_be = self._base_endpoint
        endpoint_should_be += "/%d" % self.random_id

        endpoint_to_check = self.test_class.get_chat_conversation_by_id(
            self.random_id, self.random_id)

        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_messages_for_chat_conversation(self):
        endpoint_should_be = self._base_endpoint
        endpoint_should_be += "/%d/message" % self.random_id

        endpoint_to_check = self.test_class.get_all_messages_for_chat_conversation(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_chat_attachment_by_id(self):
        endpoint_should_be = self._base_endpoint
        endpoint_should_be += "/%d/attachment/%d" % (self.random_id,
                                                     self.random_id)

        endpoint_to_check = self.test_class.get_chat_attachment_by_id(
            self.random_id, self.random_id, self.random_id)

        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_content_of_chat_attachment(self):
        endpoint_should_be = self._base_endpoint
        endpoint_should_be += "/%d/attachment/%d/content" % (
            self.random_id,
            self.random_id
        )

        endpoint_to_check = self.test_class.get_content_of_chat_attachment(
            self.random_id, self.random_id, self.random_id)

        self.assert_parameters(endpoint_should_be, endpoint_to_check)
