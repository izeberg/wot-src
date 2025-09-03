package net.wg.gui.lobby.vehPostProgression
{
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   
   public class VehPostProgressionCmpView extends VehPostProgressionViewBase
   {
       
      
      public function VehPostProgressionCmpView()
      {
         super();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerFlashComponentS(injectComponent,HANGAR_ALIASES.POST_PROGRESSION_CMP_INJECT);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         _vehicleBlock.mouseChildren = _vehicleBlock.mouseEnabled = false;
         title.mouseChildren = title.mouseEnabled = false;
      }
   }
}
