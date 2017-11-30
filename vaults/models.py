# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext as _

from fernet_fields import EncryptedCharField


class Key(models.Model):
    """Key of vaults"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    masterkey = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Back to list"""
        return reverse_lazy('vaults:open_vault')


class Vault(models.Model):
    """Vault of vaults"""

    VAULT_CATEGORY = (
        ('account', _('vault_account')),
        ('card', _('vault_card')),
        ('membership', _('vault_membership')),
        ('other', _('vault_other')),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    order = models.IntegerField(default=1)
    category = models.CharField(max_length=12, choices=VAULT_CATEGORY, default='account')
    name = EncryptedCharField(max_length=23)
    number = EncryptedCharField(max_length=64)
    valid = EncryptedCharField(max_length=20, blank=True)
    cvc = EncryptedCharField(max_length=10, blank=True)
    description = EncryptedCharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="vaults/", blank=True)

    def get_absolute_url(self):
        """Back to list"""
        return reverse_lazy('vaults:open_vault')
