from database.mongodb import connect_db
from datetime import datetime

mycol = connect_db()


def add_user(bot, cmd):
    user_dict = {
        '_id': cmd.from_user.id,
        'fname': cmd.from_user.first_name,
        'lname': cmd.from_user.last_name,
        'is_trial': True,
        'Status': 't',
        'remaining': 20,
        'date': datetime.now()
    }
    insert = mycol.insert_one(user_dict)


def find_one(bot, cmd):
    find_user = mycol.find_one({'_id': cmd.from_user.id})
    return find_user


def balance_add(bot, cmd, id, bl):
    try:
        find_use = mycol.find_one({'_id': int(id)})
        remain = find_use['remaining']
        add = mycol.find_one_and_update(
            {'_id': int(id)}, {'$set': {'remaining': int(remain) + int(bl)}})
        return True
    except TypeError as e:
        return False


def update_user(old_value, new_value):
    update_user_value = mycol.update_one(old_value, {"$set": new_value})


def trial_control(bot, cmd):
    find_one_user = find_one(bot, cmd)
    is_trial = find_one_user['is_trial']
    status = find_one_user['Status']
    remain = find_one_user['remaining']

    if is_trial and status == 't':
        if remain > 0:
            new_value = {
                'remaining': remain - 1
            }
            update_user(find_one_user, new_value)
            return True
        else:
            return False
    elif not is_trial and status == 'p':
        return True
    else:
        return 'Something went wrong'
