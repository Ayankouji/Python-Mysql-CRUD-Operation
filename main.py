from dbhelper import DBhelper


def main():
    db = DBhelper()

    while True:
        print("****WELCOME****")
        print("Press 1 to insert new user ")
        print("Press 2 to display all user ")
        print("Press 3 to delete user ")
        print("Press 4 to update user ")
        print("Press 5 to exit program ")
        print()

        try:
            choice = int(input())
            if(choice==1):
                uid = int(input("Enter User ID :"))
                username = input("Enter User Name ")
                userphone = input("Enter User Phone Number ")
                db.insert_user(uid,username,userphone)
                pass

            elif choice==2:
                db.fetch_all()
                pass

            elif choice==3:
                userid = int(input("Enter User Id which do u want to delete"))
                db.delete_user(userid)
                pass

            elif choice==4:
                uid = int(input("Enter ID of User :"))
                username = input("New Name ")
                userphone = input("New Phone Number ")
                db.update_user(uid,username,userphone)
                pass

            elif choice==5:
                break
            else:
                print("Invalid Try Again")

        except Exception as e:
            print(e)
            print("Invalid Details !Try Again !")


if __name__ == "__main__":
    main()