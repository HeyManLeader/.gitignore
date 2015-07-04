
while True:
    name = raw_input('Please input your name:')
    if name == 'George':
        passwd = raw_input('Please input passwd:')
        while passwd != '123':
            print 'Wrong passwd, Try again!'
            passwd = raw_input('Please input passwd again:')
        else:
            print 'Wlecome to the users_info system'
            while True:
                print '''
                1:Search user
                2:Add user
                3:Del user
                4:Modify
                0:Exit
                '''

                select = raw_input('Please select:').strip()
                while (select != '0') and (select != '1') and (select != '2') and (select != '3') and (select != '4'):
                    select = raw_input('Select the valid num, Try again:').strip()
                else:
                    if select == '1':
                        match = 0
                        contact_file = file('contact_list.txt','r')
                        search_name = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                        while len(search_name) == 0:
                            search_name = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                        else:
                            while True:
                                line = contact_file.readline()
                                if len(line) == 0: break
                                if search_name in line:
                                    print 'Match item: \033[36;1m%s\033[0m' % line
                                    match = 1
                                else:
                                    pass
                        if match == 0 :
                            print 'No match item found.'


                    elif select == '2':
                        contact_file = file('contact_list.txt','a')
                        add_num = raw_input('New Num:').strip()
                        while len(add_num) == 0:
                            add_num = raw_input('New Num:').strip()
                        else:
                            add_name = raw_input('New Name:').strip()
                            while len(add_name) == 0:
                                add_name = raw_input('New Name:').strip()
                            else:
                                add_dep = raw_input('New Dep:').strip()
                                while len(add_dep) == 0:
                                    add_dep = raw_input('New Dep:').strip()
                                else:
                                    contact_file.write('\n' + add_num + ' ' + add_name + ' ' + add_dep )
                        contact_file.close()
                        print add_num + ' ' + add_name + ' ' + add_dep
                        print 'Add user done!'


                    elif select == '3':
                        contact_file = file('contact_list.txt','r')
                        del_lines = contact_file.readlines()
                        contact_file.close()
                        delete = 0
                        del_name = raw_input('Del Name:').strip()
                        while len(del_name) == 0:
                            del_name = raw_input('Del Name:').strip()
                        else:
                            i = 0
                            for del_line in del_lines:
                                if del_name in del_line:
                                    temp = del_line
                                    index = i
                                    delete = 1
                                    break
                                i += 1
                            if delete == 1:
                                print 'Are you sure to delete %s' %del_name
                                ornot = raw_input('y/n:').strip()
                                while (ornot != 'y') and (ornot != 'n'):
                                    ornot = raw_input('Select again, y/n:').strip()
                                else:
                                    if ornot == 'y':
                                        del_lines.remove(temp)
                                        contact_file = file('contact_list.txt','w')
                                        for del_line in del_lines:
                                            contact_file.write(del_line)
                                        contact_file.close()
                                        print 'Delete user done!'
                            else:
                                print 'No match item found.'


                    elif select == '4':
                        contact_file = file('contact_list.txt','r')
                        mod_lines = contact_file.readlines()
                        contact_file.close()
                        print '''
                        1.Modify Num
                        2.Modify Name
                        3.Modify Dep
                        '''
                        mod_select = raw_input('Please select modify item:').strip()
                        while  (mod_select != '1') and (mod_select != '2') and (mod_select != '3'):
                            mod_select = raw_input('Select the valid num, Try again:').strip()
                        else:
                            if mod_select == '1':
                                    mod1 = 0
                                    mod_oldnum = raw_input('Old Num:').strip()
                                    while len(mod_oldnum) == 0:
                                        mod_oldnum = raw_input('Old Num:').strip()
                                    else:
                                        mod_newnum = raw_input('New Num:').strip()
                                        while len(mod_newnum) == 0:
                                            mod_newnum = raw_input('New Num:').strip()
                                        else:
                                            for mod_line in mod_lines:
                                                if mod_oldnum in mod_line:
                                                    temp1 = mod_line
                                                    temp2 = mod_line.split()
                                                    mod1 = 1
                                                    break
                                            if mod1 == 1:
                                                print 'Are you sure to modify %s' %mod_oldnum
                                                ornot = raw_input('y/n:').strip()
                                                while (ornot != 'y') and (ornot != 'n'):
                                                    ornot = raw_input('Select again, y/n:').strip()
                                                    if ornot == 'y':
                                                        i = 0
                                                        for text in temp2:
                                                            if text == mod_oldnum:
                                                                index = i
                                                                break
                                                            i += 1
                                                        temp2[index] = mod_newnum
                                                        add_line = temp2[0] + ' ' + temp2[1] + ' ' + temp2[2] + '\n'
                                                        contact_file = file('contact_list.txt','w')
                                                        for mod_line in mod_lines:
                                                            if mod_line != temp1:
                                                                contact_file.write(mod_line)
                                                            else:
                                                                contact_file.write(add_line)
                                                        contact_file.close()
                                                        print 'Modify num done!'
                                            else:
                                                print 'No match item found.'


                            elif mod_select == '2':
                                    mod2 = 0
                                    mod_oldname = raw_input('Old Name:').strip()
                                    while len(mod_oldname) == 0:
                                        mod_oldname = raw_input('Old Name:').strip()
                                    else:
                                        mod_newname = raw_input('New Name:').strip()
                                        while len(mod_newname) == 0:
                                            mod_newname = raw_input('New Name:').strip()
                                        else:
                                            for mod_line in mod_lines:
                                                if mod_oldname in mod_line:
                                                    temp1 = mod_line
                                                    temp2 = mod_line.split()
                                                    mod2 = 1
                                                    break
                                            if mod2 == 1:
                                                print 'Are you sure to modify %s' %mod_oldname
                                                ornot = raw_input('y/n:').strip()
                                                while (ornot != 'y') and (ornot != 'n'):
                                                    ornot = raw_input('Select again, y/n:').strip()
                                                else:
                                                    if ornot == 'y':
                                                        i = 0
                                                        for text in temp2:
                                                            if text == mod_oldname:
                                                                index = i
                                                                break
                                                            i += 1
                                                        temp2[index] = mod_newname
                                                        add_line = temp2[0] + ' ' + temp2[1] + ' ' + temp2[2] + '\n'
                                                        contact_file = file('contact_list.txt','w')
                                                        for mod_line in mod_lines:
                                                            if mod_line != temp1:
                                                                contact_file.write(mod_line)
                                                            else:
                                                                contact_file.write(add_line)
                                                        contact_file.close()
                                                        print 'Modify name done!'
                                            else:
                                                print 'No match item found.'


                            else:
                                    mod3 = 0
                                    mod_name = raw_input('Name:').strip()
                                    while len(mod_name) == 0:
                                        mod_name = raw_input('Name:').strip()
                                    else:
                                        mod_olddep = raw_input('Old Dep:').strip()
                                        while len(mod_olddep) == 0:
                                            mod_olddep = raw_input('Old Dep:').strip()
                                        else:
                                            mod_newdep = raw_input('New Dep:').strip()
                                            while len(mod_newdep) == 0:
                                                mod_newdep = raw_input('New Dep:').strip()
                                            else:
                                                for mod_line in mod_lines:
                                                    if mod_name in mod_line:
                                                        temp1 = mod_line
                                                        temp2 = mod_line.split()
                                                        mod3 = 1
                                                        break
                                                if mod3 == 1:
                                                    print 'Are you sure to modify %s' %mod_olddep
                                                    ornot = raw_input('y/n:').strip()
                                                    while (ornot != 'y') and (ornot != 'n'):
                                                        ornot = raw_input('Select again, y/n:').strip()
                                                    else:
                                                        if ornot == 'y':
                                                            i = 0
                                                            for text in temp2:
                                                                if text == mod_olddep:
                                                                    index = i
                                                                    break
                                                                i += 1
                                                            temp2[index] = mod_newdep
                                                            add_line = temp2[0] + ' ' + temp2[1] + ' ' + temp2[2] + '\n'
                                                            contact_file = file('contact_list.txt','w')
                                                            for mod_line in mod_lines:
                                                                if mod_line != temp1:
                                                                    contact_file.write(mod_line)
                                                                else:
                                                                    contact_file.write(add_line)
                                                            contact_file.close()
                                                            print 'Modify dep done!'
                                                else:
                                                    print 'No match item found.'


                    else:
                        break
        print 'Welcome again!'
        break

    else:
        print "Sorry, user %s not found" %name