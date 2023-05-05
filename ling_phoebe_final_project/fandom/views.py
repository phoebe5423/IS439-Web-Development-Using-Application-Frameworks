from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from fandom.forms import GroupForm, EntertainerForm, EntertainerGroupForm, AlbumForm, SongForm, CreateForm, EventForm, \
    ActivityForm
from fandom.models import Group, Entertainer, EntertainerGroup, Album, Song, Create, Event, Activity, Style

from fandom.utils import PageLinksMixin


class GroupList(PageLinksMixin, ListView, LoginRequiredMixin, PermissionRequiredMixin):
    paginate_by = 25
    model = Group
    permission_required = 'fandom.view_group'


class GroupDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Group
    permission_required = 'fandom.view_group'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        group = self.get_object()
        member_list = group.entertainer_group.all()
        context['group'] = group
        context['member_list'] = member_list
        return context


class GroupCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = GroupForm
    model = Group
    permission_required = 'fandom.add_group'


class GroupUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = GroupForm
    model = Group
    template_name = 'fandom/group_form_update.html'
    permission_required = 'fandom.change_group'


class GroupDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('fandom_group_list_urlpattern')
    permission_required = 'fandom.delete_group'

    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        members = group.entertainer_group.all()
        if members.count() > 0:
            return render(
                request,
                'fandom/group_refuse_delete.html',
                {'group': group,
                 'entertainer_groups': members,
                 }
            )
        else:
            return render(
                request,
                'fandom/group_confirm_delete.html',
                {'group': group}
            )


class EntertainerGroupList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = EntertainerGroup
    permission_required = 'fandom.view_entertainer_group'


class EntertainerGroupDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = EntertainerGroup
    permission_required = 'fandom.view_entertainer_group'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        entertainer_group = self.get_object()
        group = entertainer_group.group
        entertainer = entertainer_group.entertainer
        context['entertainer_group'] = entertainer_group
        context['group'] = group
        context['entertainer'] = entertainer
        return context


class EntertainerGroupCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = EntertainerGroupForm
    model = EntertainerGroup
    permission_required = 'fandom.add_entertainer_group'


class EntertainerGroupUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = EntertainerGroupForm
    model = EntertainerGroup
    template_name = 'fandom/entertainergroup_form_update.html'
    permission_required = 'fandom.change_entertainer_group'


class EntertainerGroupDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = EntertainerGroup
    success_url = reverse_lazy('fandom_entertainer_list_urlpattern')
    permission_required = 'fandom.delete_entertainer_group'


class EntertainerList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Entertainer
    permission_required = 'fandom.view_entertainer'


class EntertainerDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Entertainer
    permission_required = 'fandom.view_entertainer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        entertainer = self.get_object()
        company = entertainer.company
        entertainer_group_list = entertainer.entertainer_group.all()
        create_list = entertainer.create.all()
        activities_list = entertainer.activity.all()
        context['entertainer'] = entertainer
        context['company'] = company
        context['entertainer_group_list'] = entertainer_group_list
        context['create_list'] = create_list
        context['activities_list'] = activities_list
        return context


class EntertainerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = EntertainerForm
    model = Entertainer
    permission_required = 'fandom.add_entertainer'


class EntertainerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = EntertainerForm
    model = Entertainer
    template_name = 'fandom/entertainer_form_update.html'
    permission_required = 'fandom.change_entertainer'


class EntertainerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Entertainer
    success_url = reverse_lazy('fandom_entertainer_list_urlpattern')
    permission_required = 'fandom.delete_entertainer'

    def get(self, request, pk):
        entertainer = get_object_or_404(Entertainer, pk=pk)
        entertainer_groups = entertainer.entertainer_group.all()
        create = entertainer.create.all()
        activity = entertainer.activity.all()
        if entertainer_groups.count() or create.count() or activity.count() > 0:
            return render(
                request,
                'fandom/entertainer_refuse_delete.html',
                {'entertainer': entertainer,
                 'entertainer_groups': entertainer_groups,
                 'create': create,
                 'activity': activity
                 }
            )
        else:
            return render(
                request,
                'fandom/entertainer_confirm_delete.html',
                {'entertainer': entertainer}
            )


class AlbumList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Album
    permission_required = 'fandom.view_album'


class AlbumDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Album
    permission_required = 'fandom.view_album'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        album = self.get_object()
        song_list = album.song.all()
        context['entertainer'] = album
        context['song_list'] = song_list
        return context


class AlbumCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AlbumForm
    model = Album
    permission_required = 'fandom.add_album'


class AlbumUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'fandom/album_form_update.html'
    permission_required = 'fandom.change_album'


class AlbumDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('fandom_album_list_urlpattern')
    permission_required = 'fandom.delete_album'

    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        songs = album.song.all()
        if songs.count() > 0:
            return render(
                request,
                'fandom/album_refuse_delete.html',
                {'album': album,
                 'songs': songs,
                 }
            )
        else:
            return render(
                request,
                'fandom/album_confirm_delete.html',
                {'album': album}
            )


class SongList(PageLinksMixin, ListView, LoginRequiredMixin, PermissionRequiredMixin):
    paginate_by = 25
    model = Song
    permission_required = 'fandom.view_song'


class SongDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Song
    permission_required = 'fandom.view_song'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        song = self.get_object()
        create_list = song.create.all()
        context['song'] = song
        context['create_list'] = create_list
        return context


class SongCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SongForm
    model = Song
    permission_required = 'fandom.add_song'


class SongUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SongForm
    model = Song
    template_name = 'fandom/song_form_update.html'
    permission_required = 'fandom.change_song'


class SongDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('fandom_song_list_urlpattern')
    permission_required = 'fandom.delete_song'

    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        creates = song.create.all()
        if creates.count() > 0:
            return render(
                request,
                'fandom/song_refuse_delete.html',
                {'song': song,
                 'creates': creates,
                 }
            )
        else:
            return render(
                request,
                'fandom/song_confirm_delete.html',
                {'song': song}
            )


class CreateList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Create
    permission_required = 'fandom.view_create'


class CreateDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Create
    permission_required = 'fandom.view_create'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        create = self.get_object()
        entertainer = create.entertainer
        context['create'] = create
        context['entertainer'] = entertainer
        return context


class CreateCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CreateForm
    model = Create
    permission_required = 'fandom.add_create'


class CreateUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CreateForm
    model = Create
    template_name = 'fandom/create_form_update.html'
    permission_required = 'fandom.change_create'


class CreateDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Create
    success_url = reverse_lazy('fandom_song_list_urlpattern')
    permission_required = 'fandom.delete_create'


class EventList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Event
    permission_required = 'fandom.view_event'


class EventDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Event
    permission_required = 'fandom.view_event'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        event = self.get_object()
        activity_list = event.activity.all()
        context['event'] = event
        context['activity_list'] = activity_list
        return context


class EventCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = EventForm
    model = Event
    permission_required = 'fandom.add_event'


class EventUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = EventForm
    model = Event
    template_name = 'fandom/event_form_update.html'
    permission_required = 'fandom.change_event'


class EventDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('fandom_event_list_urlpattern')
    permission_required = 'fandom.delete_event'

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        activity = event.activity.all()
        if activity.count() > 0:
            return render(
                request,
                'fandom/event_refuse_delete.html',
                {'event': event,
                 'activity': activity}
            )
        else:
            return render(
                request,
                'fandom/event_confirm_delete.html',
                {'event': event}
            )


class ActivityList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Activity
    permission_required = 'fandom.view_activity'


class ActivityDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Activity
    permission_required = 'fandom.view_activity'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        activity = self.get_object()
        event = activity.event
        entertainer = activity.entertainer
        context['activity'] = activity
        context['event'] = event
        context['entertainer'] = entertainer
        return context


class ActivityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ActivityForm
    model = Activity
    permission_required = 'fandom.add_activity'


class ActivityUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ActivityForm
    model = Activity
    template_name = 'fandom/activity_form_update.html'
    permission_required = 'fandom.change_activity'


class ActivityDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('fandom_event_list_urlpattern')
    permission_required = 'fandom.delete_activity'

    def get(self, request, pk):
        activity = get_object_or_404(Activity, pk=pk)
        return render(
                request,
                'fandom/activity_confirm_delete.html',
                {'activity': activity}
            )


class StyleList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Style
    permission_required = 'fandom.view_style'


class StyleDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Style
    permission_required = 'fandom.view_style'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        style = self.get_object()
        album_list = style.album.all()
        song_list = style.song.all()
        event_list = style.event.all()
        context['style'] = style
        context['album_list'] = album_list
        context['song_list'] = song_list
        context['event_list'] = event_list
        return context
