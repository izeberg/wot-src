from __future__ import absolute_import
from ac_visual_script_client import blocks
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.HANGAR)
g_blockRegistrar.regBlocksFromModule(blocks)