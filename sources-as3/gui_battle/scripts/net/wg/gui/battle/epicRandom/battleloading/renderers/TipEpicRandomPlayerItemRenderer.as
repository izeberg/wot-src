package net.wg.gui.battle.epicRandom.battleloading.renderers
{
   import net.wg.data.constants.UserTags;
   
   public class TipEpicRandomPlayerItemRenderer extends EpicRandomBasePlayerItemRenderer
   {
       
      
      public function TipEpicRandomPlayerItemRenderer()
      {
         super();
      }
      
      override protected function setSelfBG() : void
      {
         if(selfBg != null)
         {
            selfBg.visible = UserTags.isCurrentPlayer(model.userTags);
            if(selfBg.visible)
            {
               selfBg.source = RES_ICONS.MAPS_ICONS_BATTLELOADING_SELFTIPSBG;
            }
         }
      }
   }
}
