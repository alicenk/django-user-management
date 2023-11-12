from django.http import JsonResponse
from rest_framework import generics
from userpreferences.services.sectors_services import SectorsService


class SectorsCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        sector_data = request.data
        created_sector_data = SectorsService.create_sector(sector_data)
        return JsonResponse({
            "message": "Sektör oluşturacak",
            "sector_data": created_sector_data
        })


class SectorsListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        sectors = SectorsService.list_sectors()
        return JsonResponse({
            "message": "Sektör listeleyecek",
            "sectors": sectors
        })


class SectorsUpdateView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        sector_id = kwargs.get('sector_id')
        updated_data = request.data
        updated_sector_data = SectorsService.update_sectors(sector_id, updated_data)
        if updated_sector_data:
            return JsonResponse({
                "message": "Sektör bilgisi güncellenecek",
                "sector_data": updated_sector_data
            })
        else:
            return JsonResponse({
                "message": f"Sektör {sector_id} bulunamadı"
            }, status=404)


class SectorsDeleteView(generics.DestroyAPIView):
    lookup_url_kwarg = 'sector_id'

    def delete(self, request, *args, **kwargs):
        sector_id = kwargs.get(self.lookup_url_kwarg)
        if SectorsService.delete_sector(sector_id):
            return JsonResponse({
                "message": f"Sektör {sector_id} silindi"
            })
        else:
            return JsonResponse({
                "message": f"Sektör {sector_id} bulunamadı"
            }, status=404)