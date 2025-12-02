from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
from grinch_common.visual_script_common import arena_blocks
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.SERVER)
g_blockRegistrar.regBlocksFromModule(arena_blocks)