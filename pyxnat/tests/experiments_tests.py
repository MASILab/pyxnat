import os.path as op
from .. import Interface
from . import skip_if_no_network

_modulepath = op.dirname(op.abspath(__file__))

central = Interface(config=op.join(op.dirname(op.abspath(__file__)), 'central.cfg'))

@skip_if_no_network
def test_global_experiment_listing():
    assert central.array.experiments(project_id='CENTRAL_OASIS_CS',
                                     experiment_type='xnat:mrSessionData',
                                     )
