import datetime

from weather import models

from rest_framework import serializers


class KhTemperatureSerializer(serializers.ModelSerializer):
    month = serializers.SerializerMethodField(read_only=True)
    year = serializers.SerializerMethodField(read_only=True)

    def get_month(self, obj):
        return obj.date.strftime("%m")

    def get_year(self, obj):
        return obj.date.strftime("%Y")

    class Meta:
        model = models.KhTmax
        fields = ("year", "value", "month")


class KhMinTemperatureSerializer(serializers.ModelSerializer):

    def get_month(self, obj):
        return obj.date.strftime("%m")

    def get_year(self, obj):
        return obj.date.strftime("%Y")

    class Meta:
        model = models.KhTmin
        fields = ("year", "value", "month")


class KhRainFallSerializer(serializers.ModelSerializer):

    def get_month(self, obj):
        return obj.date.strftime("%m")

    def get_year(self, obj):
        return obj.date.strftime("%Y")

    class Meta:
        model = models.KhRainFall
        fields = ("year", "value", "month")


class KhAddTemperatureSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=255)
    data = serializers.JSONField()
    level = serializers.CharField(max_length=10)

    def save(self, **kwargs):
        country = self.validated_data.get("country")
        bulk_temp = []
        for item in self.validated_data.get("data"):
            #
            try:
                date_str = "{0}{1}{2}".format(item.get("year"), "01", item.get("month"))
                datetime_obj = datetime.datetime.strptime(date_str, '%Y%d%m')
                d = {"country": country, "value": item.get("value"), "date": datetime_obj.date()}
            except:
                raise serializers.ValidationError({"data":
                                                       ["Invalid JSON format. e.g {value:32, year:1990, month:3}"]})

            t = KhTemperatureSerializer(data=d)
            t.is_valid(raise_exception=True)
            if self.validated_data.get("level") == "max":
                bulk_temp.append(models.KhTmax(**d))
                ts = models.KhTmax.objects.bulk_create(bulk_temp)
            else:
                bulk_temp.append(models.KhTmin(**d))
                ts = models.KhTmin.objects.bulk_create(bulk_temp)

        return ts


class KhAddRainfallSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=255)
    data = serializers.JSONField()

    def save(self, **kwargs):

        country = self.validated_data.get("country")
        bulk_temp = []
        for item in self.validated_data.get("data"):
            try:
                date_str = "{0}{1}{2}".format(item.get("year"), item.get("month"), "01")
                datetime_obj = datetime.datetime.strptime(date_str, '%Y%d%m')
                d = {"country": country, "value": item.get("value"), "date": datetime_obj.date()}
            except:
                raise serializers.ValidationError({"data": ["Invalid JSON format. e.g {value:32, year:1990, month:3}"]})

            t = KhRainFallSerializer(data=d)
            t.is_valid(raise_exception=True)
            bulk_temp.append(models.KhRainFall(**d))

        ts = models.KhRainFall.objects.bulk_create(bulk_temp)

        return ts



