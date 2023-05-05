from django.urls import path

from fandom.views import (
    GroupList, GroupDetail, GroupCreate, GroupUpdate, GroupDelete,
    EntertainerList, EntertainerDetail, EntertainerCreate, EntertainerUpdate, EntertainerDelete,
    EntertainerGroupList, EntertainerGroupDetail, EntertainerGroupCreate, EntertainerGroupUpdate, EntertainerGroupDelete,
    AlbumList, AlbumDetail, AlbumCreate, AlbumUpdate, AlbumDelete,
    SongList, SongDetail, SongCreate, SongUpdate, SongDelete,
    CreateList, CreateDetail, CreateCreate, CreateUpdate, CreateDelete,
    ActivityList, ActivityDetail, ActivityCreate, ActivityUpdate, ActivityDelete,
    EventList, EventDetail, EventCreate, EventUpdate, EventDelete,
    StyleList, StyleDetail
)

urlpatterns = [

    path('group/', GroupList.as_view(),
         name='fandom_group_list_urlpattern'),

    path('group/<int:pk>', GroupDetail.as_view(),
         name='fandom_group_detail_urlpattern'),

    path('group/create/',
         GroupCreate.as_view(),
         name='fandom_group_create_urlpattern'),

    path('group/<int:pk>/update',
         GroupUpdate.as_view(),
         name='fandom_group_update_urlpattern'),

    path('group/<int:pk>/delete',
         GroupDelete.as_view(),
         name='fandom_group_delete_urlpattern'),

    path('entertainer/', EntertainerList.as_view(),
         name='fandom_entertainer_list_urlpattern'),

    path('entertainer/<int:pk>', EntertainerDetail.as_view(),
         name='fandom_entertainer_detail_urlpattern'),

    path('entertainer/create/',
         EntertainerCreate.as_view(),
         name='fandom_entertainer_create_urlpattern'),

    path('entertainer/<int:pk>/update',
         EntertainerUpdate.as_view(),
         name='fandom_entertainer_update_urlpattern'),

    path('entertainer/<int:pk>/delete',
         EntertainerDelete.as_view(),
         name='fandom_entertainer_delete_urlpattern'),

    path('entertainer_group/', EntertainerGroupList.as_view(),
         name='fandom_entertainergroup_list_urlpattern'),

    path('entertainer_group/<int:pk>', EntertainerGroupDetail.as_view(),
         name='fandom_entertainergroup_detail_urlpattern'),

    path('entertainer_group/create/',
         EntertainerGroupCreate.as_view(),
         name='fandom_entertainergroup_create_urlpattern'),

    path('entertainer_group/<int:pk>/update',
         EntertainerGroupUpdate.as_view(),
         name='fandom_entertainergroup_update_urlpattern'),

    path('entertainer_group/<int:pk>/delete',
         EntertainerGroupDelete.as_view(),
         name='fandom_entertainergroup_delete_urlpattern'),

    path('album/', AlbumList.as_view(),
         name='fandom_album_list_urlpattern'),

    path('album/<int:pk>', AlbumDetail.as_view(),
         name='fandom_album_detail_urlpattern'),

    path('album/create/', AlbumCreate.as_view(),
         name='fandom_album_create_urlpattern'),

    path('album/<int:pk>/update', AlbumUpdate.as_view(),
         name='fandom_album_update_urlpattern'),

    path('album/<int:pk>/delete', AlbumDelete.as_view(),
         name='fandom_album_delete_urlpattern'),

    path('song/', SongList.as_view(),
         name='fandom_song_list_urlpattern'),

    path('song/<int:pk>', SongDetail.as_view(),
         name='fandom_song_detail_urlpattern'),

    path('song/create/', SongCreate.as_view(),
         name='fandom_song_create_urlpattern'),

    path('song/<int:pk>/update', SongUpdate.as_view(),
         name='fandom_song_update_urlpattern'),

    path('song/<int:pk>/delete', SongDelete.as_view(),
         name='fandom_song_delete_urlpattern'),

    path('create/', CreateList.as_view(),
         name='fandom_create_list_urlpattern'),

    path('create/<int:pk>', CreateDetail.as_view(),
         name='fandom_create_detail_urlpattern'),

    path('create/create/', CreateCreate.as_view(),
         name='fandom_create_create_urlpattern'),

    path('create/<int:pk>/update', CreateUpdate.as_view(),
         name='fandom_create_update_urlpattern'),

    path('create/<int:pk>/delete', CreateDelete.as_view(),
         name='fandom_create_delete_urlpattern'),

    path('event/', EventList.as_view(),
         name='fandom_event_list_urlpattern'),

    path('event/<int:pk>', EventDetail.as_view(),
         name='fandom_event_detail_urlpattern'),

    path('event/create/', EventCreate.as_view(),
         name='fandom_event_create_urlpattern'),

    path('event/<int:pk>/update', EventUpdate.as_view(),
         name='fandom_event_update_urlpattern'),

    path('event/<int:pk>/delete', EventDelete.as_view(),
         name='fandom_event_delete_urlpattern'),

    path('activity/', ActivityList.as_view(),
         name='fandom_activity_list_urlpattern'),

    path('activity/<int:pk>', ActivityDetail.as_view(),
         name='fandom_activity_detail_urlpattern'),

    path('activity/create/', ActivityCreate.as_view(),
         name='fandom_activity_create_urlpattern'),

    path('activity/<int:pk>/update', ActivityUpdate.as_view(),
         name='fandom_activity_update_urlpattern'),

    path('activity/<int:pk>/delete', ActivityDelete.as_view(),
         name='fandom_activity_delete_urlpattern'),

    path('style/', StyleList.as_view(),
         name='fandom_style_list_urlpattern'),

    path('style/<int:pk>', StyleDetail.as_view(),
         name='fandom_style_detail_urlpattern'),

]
