package net.wg.gui.battle.views.decorativeCrosshair
{
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.infrastructure.base.meta.impl.ConcentrationDecorativeCrosshairMeta;
   import net.wg.utils.StageSizeBoundaries;
   
   public class ConcentrationDecorativeCrosshair extends ConcentrationDecorativeCrosshairMeta
   {
      
      private static const ARCADE_SCALE:Number = 0.67;
      
      private static const SNIPER_SCALE:Number = 1;
      
      private static const NORMAL_SCALE:Number = 0.85;
       
      
      public function ConcentrationDecorativeCrosshair()
      {
         super();
      }
      
      override public function updateScale(param1:int) : void
      {
         if(param1 == CROSSHAIR_VIEW_ID.ARCADE)
         {
            if(App.appWidth < StageSizeBoundaries.WIDTH_1920)
            {
               setScale(ARCADE_SCALE);
            }
            else
            {
               setScale(NORMAL_SCALE);
            }
         }
         else if(param1 == CROSSHAIR_VIEW_ID.SNIPER)
         {
            if(App.appWidth >= StageSizeBoundaries.WIDTH_1920)
            {
               setScale(SNIPER_SCALE);
            }
            else
            {
               setScale(NORMAL_SCALE);
            }
         }
      }
   }
}
