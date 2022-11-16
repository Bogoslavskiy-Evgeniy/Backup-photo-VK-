from Yandex_disk import Yandex_disk
from Backup_photo import Backup_photo

if __name__ == '__main__':
    Token_yandex = .....
    id_VK = .....
    backup = Backup_photo(id_VK)
    uploader = Yandex_disk(Token_yandex)
    photo_list = backup.list_photo()
    uploader.upload_photo_to_disk(photo_list)
    backup.photo_json()







