PIPELINE_CSS = {
    'hado_base_css': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/style.css',
            'css/datepicker.css',
            'css/bootstrap-responsive.css',
        ),
        'output_filename': 'dist/hado.css',
    },
    'hado_admin_css': {
        'source_filenames': (
            'css/admin.css',
        ),
        'output_filename': 'dist/hdadmin.css',
    },
}

PIPELINE_JS = {
    'hado_base_js': {
        'source_filenames': (
            'js/jquery-1.10.1.min.js',
            'js/bootstrap.js',
            'js/bootstrap-datepicker.js',
        ),
        'output_filename': 'dist/hado.base.js',
    },
    'hado_register_js': {
        'source_filenames': (
            "js/register.js",
        ),
        'output_filename': 'dist/hado.register.js',
    },
    'hado_home_js': {
        'source_filenames': (
            'js/jquery.cookie.js',
            'js/user_home.js',
        ),
        'output_filename': 'dist/hado.home.js',
    },
}
