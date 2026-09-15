from django.contrib import admin
from .models import chaiVerity , chaiReview , Store , chaiCertificate  # yeha pe hamne chaiVerity model ko import kiya hai taki ham usko admin panel me register kar sakein


# Register your models here.

class chaiReviewInline(admin.TabularInline): # yeha pe hamne chaiReviewInline class ko define kiya hai taki ham chaiVerity model ke saath chaiReview model ko inline me show kar sakein
    model = chaiReview # yeha pe hamne chaiReview model ko inline me show karne ke liye define kiya hai
    extra = 2 # yeha pe hamne extra attribute ko define kiya hai taki ham chaiVerity model ke saath chaiReview model ke liye ek extra form show kar sakein


class chaiVerityAdmin(admin.ModelAdmin): # yeha pe hamne chaiVerityAdmin class ko define kiya hai taki ham chaiVerity model ke liye admin panel me customizations kar sakein
    list_display = ('name', 'type', 'date_added') # yeha pe hamne list_display attribute ko define kiya hai taki ham chaiVerity model ke liye admin panel me list view me name, type aur date_added fields ko show kar sakein
    search_fields = ('name', 'type') # yeha pe hamne search_fields attribute ko define kiya hai taki ham chaiVerity model ke liye admin panel me search functionality ko enable kar sakein aur name aur type fields ke basis pe search kar sakein
    inlines = [chaiReviewInline] # yeha pe hamne inlines attribute ko define kiya hai taki ham chaiVerity model ke saath chaiReview model ko inline me show kar sakein


class storeAdmin(admin.ModelAdmin): # yeha pe hamne storeAdmin class ko define kiya hai taki ham Store model ke liye admin panel me customizations kar sakein
    list_display = ('name', 'location') # yeha pe hamne list_display attribute ko define kiya hai taki ham Store model ke liye admin panel me list view me name aur location fields ko show kar sakein
    # search_fields = ('name', 'location') # yeha pe hamne search_fields attribute ko define kiya hai taki ham Store model ke liye admin panel me search functionality ko enable kar sakein aur name aur location fields ke basis pe search kar sakein
    filter_horizontal = ('chair_verities',) # yeha pe hamne filter_horizontal attribute ko define kiya hai taki ham Store model ke liye admin panel me chair_verity field ke liye horizontal filter ko enable kar sakein


class chaiCertificateAdmin(admin.ModelAdmin): # yeha pe hamne chaiCertificateAdmin class ko define kiya hai taki ham chaiCertificate model ke liye admin panel me customizations kar sakein
    list_display = ('chai', 'certificate_number', 'issue_date', 'valid_until') # yeha pe hamne list_display attribute ko define kiya hai taki ham chaiCertificate model ke liye admin panel me list view me chai, certificate_number, issue_date aur valid_until fields ko show kar sakein
    search_fields = ('chai__name', 'certificate_number') # yeha pe hamne search_fields attribute ko define kiya hai taki ham chaiCertificate model ke liye admin panel me search functionality ko enable kar sakein aur chai ke name aur certificate_number fields ke basis pe search kar sakein

admin.site.register(chaiVerity, chaiVerityAdmin) # yeha pe hamne chaiVerity model ko admin panel me register kiya hai taki ham usko admin panel me access kar sakein
admin.site.register(Store, storeAdmin) # yeha pe hamne Store model ko admin panel me register kiya hai taki ham usko admin panel me access kar sakein
admin.site.register(chaiCertificate, chaiCertificateAdmin) # yeha pe hamne chaiCertificate model ko admin panel me register kiya hai taki ham usko admin panel me access kar sakein

