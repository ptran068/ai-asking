from rest_framework import serializers
from email_store.models import EmailStoreModel
import arrow


class EmailStoreSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) # customize format, unique error if needed

    class Meta:
        model = EmailStoreModel
        fields = "__all__"


class ListEmailStoreSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = EmailStoreModel
        fields = "__all__"

    def get_created_at(self, instance):
        created_at = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return arrow.get(created_at).humanize()
