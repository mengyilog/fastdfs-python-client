> ================================================================
>    Copyright (C) 2015 All rights reserved.
>
>    filename:interfaces.md
>
>    author:sulit sulitsrc@163.com
>
>    modify date,time:2015-05-27 09:41
>
>    discription:
>
> ================================================================

1. fdfs_init(conf_filename)

  初始化fdfs客户端，conf_filename为fdfs客户端配置文件，如果要使用fdfspyclient，在使用前必须进行初始化，初始化成功返回0，失败返回错误值。

2. fdfs_upload(local_filename, upload_typestr | None)

  上传文件，localfilename为本地要上传的文件，upload_typestr为上传形式，有三种，FILE，BUFF，CALLBACK，默认是FILE，如果不指定，请给upload_typestr赋值为None。上传成功返回０，失败返回失败错误值。

  返回值，result为执行结果是否成功，group_name为上传到的组名，remote_filename为远程文件名，file_url为文件url地址。

3. fdfs_download(group_name, remote_filename, local_filename | None)

  下载文件，group_name为下载文件的组名，remote_filename为远程文件名，local_filename为下载下载来存到本地的文件名，如果不指定，请用None代替，这时会生成和远程文件名一样的文件

  返回值，result为执行结果是否成功，local_filename为是否保存到本地的文件名，file_size为文件大小

4. fdfs_delete(group_name, remote_filename)

  删除文件，group_name为删除文件的组名，remote_filename为远程文件名

  返回值，result为执行结果是否成功

5. fdfs_getmeta(group_name, remote_filename)

  获得一个文件的元信息，group_name为组名，remote_filename为远程文件名

  返回值，result为执行结果是否成功，meta_count为元信息数，metatable为元信息表，这个传给python的是个元组，每一项为name=value形式的字符串，如果需要其中的信息，请自行分解。


5. fdfs_setmeta(group_name, remote_filename, op_flag, metadata_list)

  设置文件元信息，group_name为组名，remote_filename为远程文件名，op_flag为操作方式，O代表重写，M代表合并，metadata_list为设置的元信息表。metadata_list应该是name1=value1,name2=value2,...形式的。

  返回值，result为执行结果是否成功

6. fdfs_query_servers(group_name, remote_filename)

  查询服务器，group_name为组名，remote_filename为远程文件名

  返回值，result为执行结果是否成功，server_count为存储服务器数，storageServertable为存储服务器列表，存储服务器列表返回给python的是元组

7. fdfs_append_file(appender_file_id, local_filename)

  追加文件，appender_file_id为组名加远程文件名表示的信息，例如group1/M00/00/00/wKj_gVVlJVSAJ9SCAAAAAAAAAAA6108.db，这个是要追加的文件ID，local_filename为本地文件名

  返回值，result为执行结果是否成功

8. fdfs_file_info(file_id)

  查询文件信息，file_id为组名加远程文件名，前面给出过例子

  返回值，result为执行结果是否成功，fileinfotable为返回的文件信息表，是个元组

9. fdfs_upload_append(local_filename)

  追加上传，local_filename为本地文件名

  返回值，result为执行结果是否成功，file_id为文件ID，这个应该是组名+远程文件名

10. fdfs_list_all_groups(tracker_server | None, group_name | None)

  列出所有的组，tracker_server为跟踪服务器，group_name为组名，这两个值，都可以为空，当为空时，用None代替。

  返回值，result为执行结果是否成功

11. fdfs_delete_group(tracker_server | None, group_name)

  删除指定组，tracker_server为跟踪服务器，可以为空，当为空时，用None代替，group_name为组名。

  返回值，result为执行结果是否成功

12. fdfs_delete_server(tracker_server | None, group_name, storage_id)

  删除服务器，tracker_server为跟踪服务器，可以为空，当为空时，用None代替，group_name为组名，storage_id为服务器id

  返回值，result为执行结果是否成功

13. fdfs_set_trunk_server()

  设置根服务器，tracker_server为跟踪服务器，可以为空，当为空时，用None代替，group_name为组名，storage_id为服务器id

  返回值，result为执行结果是否成功，new_trunk_server_id为新的根服务器ID

14. fdfs_destroy()

  杀死客户端程序。
