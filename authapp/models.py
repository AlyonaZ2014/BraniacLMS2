username = models.CharField(
    _("username"),
    max_length=150,
    unique=True,
    help_text=_("Required. 150 characters or fewer. ASCII letters and digits only."),
    validators=[username_validator],
    error_messages={
        "unique": _("A user with that username already exists."),
    },
)
