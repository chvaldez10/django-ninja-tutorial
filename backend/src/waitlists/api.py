from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema
from .models import WaitlistEntry

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.get("{entry_id}/", response=WaitlistEntryDetailSchema)
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return {
        "id": obj.id,
        "email": obj.email,
        "updated": obj.updated,
        "timestamp": obj.timestamp,
    }