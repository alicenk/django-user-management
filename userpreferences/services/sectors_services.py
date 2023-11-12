from userpreferences.models import Sector
from userpreferences.serializers import SectorSerializer

class SectorsService:
    @staticmethod
    def create_sector(sector_data):
        serializer = SectorSerializer(data=sector_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def list_sectors():
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return serializer.data

    @staticmethod
    def update_sectors(sectors_id, updated_data):
        try:
            sectors = Sector.objects.get(pk=sectors_id)
            serializer = SectorSerializer(instance=sectors, data=updated_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data
        except Sector.DoesNotExist:
            return None

    @staticmethod
    def delete_sector(sector_id):
        try:
            sector = Sector.objects.get(pk=sector_id)
            sector.delete()
            return True
        except Sector.DoesNotExist:
            return False