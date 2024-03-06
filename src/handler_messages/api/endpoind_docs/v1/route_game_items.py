SEND_MESSAGE_RESPONSES = {
    400: {
        'description': """
        1. Invalid bot token
        2. Invalid chat it
        """,
        'content': {
            'application/json': {
                'examples': {
                    '1': {
                        'summary': 'Invalid bot token',
                        'value': {'detail': "Invalid bot token: %s"}
                    },
                    '2': {
                        'summary': 'Invalid chat id',
                        'value': {'detail': "Invalid chat id: %s"}
                    },
                },
            }
        }
    },
}
