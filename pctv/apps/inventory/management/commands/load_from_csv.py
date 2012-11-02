import sys
from django.core.management.base import BaseCommand, CommandError
import datetime
import csv

from apps.inventory.models import Inventory, Condo, Prototype, Section


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        path = "/Users/axolote/Workspace/kiwisplice/csv/in/inventory.csv"
        reader = csv.DictReader(open(path))

        # Now just store everything in the DB
        for l in reader:
            for key, val in l.items():
                l[key.strip()] = val.strip()
            # first create the condo if it's not there
            condo = Condo.objects.get_or_create(name=l["Condominio"])[0]
            prototype = Prototype.objects.get_or_create(name=l["Prototipo"])[0]
            section = Section.objects.get_or_create(name=l["ETAPAS"])[0]

            # Now the new inventory entry
            inventory = Inventory(
                prototype=prototype,
                section=section,
                construction_status=l["Status construccion"].lower().capitalize(),
                cuv=l["CUV"],
                number=l["Num Oficial"],
                block=l["Manz"],
                macro_lot=l["Macro Lote"],
                lot=l["Lote"],
                condo=condo,
                official_id=l["No."],
                lot_size=l["M2 Terreno"],
                construction_size=l["M2 Constr."],
                construction_end_date=datetime.datetime.strptime(l["fecha contruccion"], "%d/%m/%y"),
                percent_completed=int(l["por. Completado"].replace("%", "")),
                siapa_account=l["cuenta SIAPA"],
                predial_account=l["CUENTA PREDIAL"],
                clg_folium=l["FOLIO CLG"],
                predial_payment_date=datetime.datetime.strptime(l["FECHA PREDIAL"], "%d/%m/%y"),
                siapa_payment_date=datetime.datetime.strptime(l["FECHA SIAPA"], "%d/%m/%y"),
                clg_emission_date=datetime.datetime.strptime(l["FECHA CLG"], "%d/%m/%y"),
                price=l["PRECIO"]
            )

            inventory.save()
            print "Inmueble con pk %d ha sido creado" % inventory.pk
