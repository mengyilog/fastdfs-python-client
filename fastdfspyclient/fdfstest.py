#============================================
#   Copyright (C) 2015 All rights reserved.
#
#   filename : fdfstest.py
#   author : sulit - sulitsrc@163.com
#   last modified : 2015-05-24 09:12
#   description : fastpyclient test program
#
#============================================

#!/usr/bin/python

import fdfspyclient

# 1
print "init"
fdfspyclient.fdfs_init("client.conf")

# 2
print "upload"
result, groupname, remotefilename, fileurl = fdfspyclient.fdfs_upload("Makefile", None)
print result, groupname, remotefilename, fileurl

# 3
print "download"
result, localfilename, filesize = fdfspyclient.fdfs_download(groupname, remotefilename, None)
print result, localfilename, filesize

# 4
print "getmeta"
ret, ocount, o = fdfspyclient.fdfs_getmeta(groupname, remotefilename)
print ret, ocount, o

# 5
print "setmeta"
ret = fdfspyclient.fdfs_setmeta(groupname, remotefilename, "O", "name=sulit,value=1")
print ret

# 4
print "getmeta"
ret, ocount, o = fdfspyclient.fdfs_getmeta(groupname, remotefilename)
print ret, ocount, o

# 6
print "query_servers"
ret, servercount, storageServertable = fdfspyclient.fdfs_query_servers(groupname, remotefilename)
print ret, servercount, storageServertable

# 7 and 8
print "upload_append"
ret, fileid = fdfspyclient.fdfs_upload_append("Makefile")
print ret, fileid

# 8 and 7
print "append file"
ret = fdfspyclient.fdfs_append_file(fileid, "Makefile")
print ret

# 9
print "file info"
ret, fileinfotable = fdfspyclient.fdfs_file_info(groupname+"/"+remotefilename)
print ret, fileinfotable

# 10
print "delete file"
ret = fdfspyclient.fdfs_delete(groupname, remotefilename)
print ret

## 11
#print "list all groups"
#ret = fdfspyclient.fdfs_list_all_groups(None, None)
#print ret

## 12
#print "list one groups"
#ret = fdfspyclient.fdfs_list_all_groups(None, groupname)
#print ret

## 13
#ret = fdfspyclient.fdfs_delete_server(None, groupname, "0")
#print ret

## 14
#ret = fdfspyclient.fdfs_delete_group(None, groupname)
#print ret

## 15 fdfs_set_trunk_server

# 16
fdfspyclient.fdfs_destroy()
