import vk_api
from info import *


def two_fa():
    fa_code = input("2FA Code: ")
    remember = bool(int(input("Remember this device? (1/0): ")))
    return fa_code, remember


def nuke_by_q(vk_session):
    query = input("По какому слову уничтожать?: ")
    msgs = vk_session.method("messages.search", {"q": query})
    print(msgs)

    results_count = msgs['count']
    del_count = 0
    print(f"Найдено совпадений: {results_count}")

    print(msgs['items'])
    del_for_all = int(input("Удалить для всех (если <24 часов)? (1/0): "))
    del_from_everyone = int(input("Удалить сообщения всех пользователей? (1 = от всех/0 = только свои): "))

    if int(input("Подтвердить? (1/0): ")):
        for msg in msgs['items']:
            if del_from_everyone:                   # Удаление сообщений от всех пользователей
                try:
                    status = vk_session.method("messages.delete", {'message_ids': msg['id'], 'delete_for_all': del_for_all})
                except vk_api.ApiError:
                    status = vk_session.method("messages.delete", {'message_ids': msg['id']})

                if status[str(msg['id'])] != 1:
                    print(f"Ошибка {status[str(msg['id'])]} при удалении сообщения, id = {msg['id']}")
                else:
                    del_count += 1
            elif msg['from_id'] == int(user_id):    # Удаление только своих сообщений
                try:
                    status = vk_session.method("messages.delete",
                                               {'message_ids': msg['id'], 'delete_for_all': del_for_all})
                except vk_api.ApiError:
                    status = vk_session.method("messages.delete", {'message_ids': msg['id']})

                if status[str(msg['id'])] != 1:
                    print(f"Ошибка {status[str(msg['id'])]} при удалении сообщения, id = {msg['id']}")
                else:
                    del_count += 1
    else:
        print("Отмена")
    print(f"Завершено. Удалено {del_count} из {results_count} совпадений.")


def main():
    # pwd = input("Password: ")

    vk_session = vk_api.VkApi(user_login, pwd, auth_handler=two_fa, app_id=6121396, api_version=api_version)
    try:
        vk_session.auth()
    except Exception as error_msg:
        print(error_msg)
        print("ERROR: in vk_session:", vk_session)
        return

    vk = vk_session.get_api()
    nuke_by_q(vk_session)


if __name__ == '__main__':
    main()
