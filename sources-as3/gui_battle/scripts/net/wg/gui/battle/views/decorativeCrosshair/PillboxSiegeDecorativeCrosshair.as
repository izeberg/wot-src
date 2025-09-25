package net.wg.gui.battle.views.decorativeCrosshair
{
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.infrastructure.base.meta.impl.PillboxSiegeDecorativeCrosshairMeta;
   import net.wg.utils.StageSizeBoundaries;
   
   public class PillboxSiegeDecorativeCrosshair extends PillboxSiegeDecorativeCrosshairMeta
   {
      
      private static const ARCADE_SCALE:Number = 0.8;
      
      private static const ARCADE_SCALE_SMALL:Number = 0.65;
      
      private static const SNIPER_SCALE:Number = 1;
      
      private static const SNIPER_SCALE_SMALL:Number = 0.72;
       
      
      public function PillboxSiegeDecorativeCrosshair()
      {
         super();
      }
      
      override public function updateScale(param1:int) : void
      {
         if(param1 == CROSSHAIR_VIEW_ID.ARCADE)
         {
            if(App.appWidth < StageSizeBoundaries.WIDTH_1920)
            {
               setScale(ARCADE_SCALE_SMALL);
            }
            else
            {
               setScale(ARCADE_SCALE);
            }
         }
         else if(param1 == CROSSHAIR_VIEW_ID.SNIPER)
         {
            if(App.appWidth < StageSizeBoundaries.WIDTH_1920)
            {
               setScale(SNIPER_SCALE_SMALL);
            }
            else
            {
               setScale(SNIPER_SCALE);
            }
         }
      }
   }
}
