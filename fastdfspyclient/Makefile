#============================================
#   Copyright (C) 2015 All rights reserved.
#
#   filename : Makefile
#   author : sulit - sulitsrc@163.com
#   last modified : 2015-05-24 07:10
#   description :
#
#============================================

.SUFFIXES: .c .o

COMPILE = gcc -Wall -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -g -O -DDEBUG_FLAG -DOS_LINUX -DIOEVENT_USE_EPOLL
INC_PATH = -I. -I../../tracker -I../../storage -I../ -I ../../common -I/usr/include -I/usr/include/python2.7 -I/usr/include/fastcommon -I/usr/include/fdfsdfst
LIB_PATH = -L/usr/local/lib -L../ -lfastcommon  -lfdfsclient  -lpthread -ldl -rdynamic
FDFS_SRC_FILES = fdfspyclient.c
#FDFS_SRC_FILES = fastdfstest.c
FDFS_SHARED_OBJS = fdfspyclient.o
#FDFS_SHARED_OBJS = fastdfstest.o
FDFS_DEST_SHARED_LIBS = fdfspyclient.so

$(FDFS_DEST_SHARED_LIBS): $(FDFS_SHARED_OBJS)
	$(COMPILE) -shared $(LIB_PATH) -o $@ $^
$(FDFS_SHARED_OBJS): $(FDFS_SRC_FILES)
	$(COMPILE) -c -fPIC $^ $(INC_PATH) $(LIB_PATH)

clean:
	rm -rf *.o *.so
