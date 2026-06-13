import logging

_logger = logging.getLogger(__name__)
def migrate(cr, version):
    _logger.info("Forzamos la actualización de los l10n_latam_move_check_ids_operation_date")
    #cr.execute("COMMENT ON INDEX l10n_latam_check_unique IS 'index marked to upgrade'")
    cr.execute("""
        UPDATE l10n_latam_check
           SET payment_date = create_date::date
         WHERE id = 1400
           AND payment_date IS NULL
    """)
    _logger.warning("Set payment_date to create_date for l10n_latam_check with id 1400")
