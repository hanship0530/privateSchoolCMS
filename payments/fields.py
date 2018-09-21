from django.forms import ModelChoiceField

# Create your field here.
class SubjectModelChoiceField(ModelChoiceField):
	def lable_from_instance(self, obj):
		return obj.item

class PriceModelChoiceField(ModelChoiceField):
	def lable_from_instance(self, obj):
		return int(obj.price)
