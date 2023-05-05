from django import forms

from fandom.models import Group, Entertainer, EntertainerGroup, Album, Song, Create, Event, Activity


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def clean_group_name(self):
        return self.cleaned_data['group_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class EntertainerForm(forms.ModelForm):
    class Meta:
        model = Entertainer
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class EntertainerGroupForm(forms.ModelForm):
    class Meta:
        model = EntertainerGroup
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def clean_album_name(self):
        return self.cleaned_data['album_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    def clean_song_name(self):
        return self.cleaned_data['song_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def clean_event_name(self):
        return self.cleaned_data['event_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


class EntertainerGroupForm(forms.ModelForm):
    class Meta:
        model = EntertainerGroup
        fields = '__all__'
