package net.wg.gui.battle.bob
{
   import net.wg.data.constants.UserTags;
   import net.wg.gui.battle.battleloading.renderers.BaseRendererContainer;
   import net.wg.gui.battle.bob.data.BobDAAPIVehicleInfoVO;
   import net.wg.gui.battle.random.battleloading.renderers.RandomPlayerItemRenderer;
   
   public class BobTablePlayerItemRenderer extends RandomPlayerItemRenderer
   {
      
      private static const BLOGGER_COLOR_SCHEME_PREFIX:String = "blogger_";
       
      
      public function BobTablePlayerItemRenderer(param1:BaseRendererContainer, param2:int, param3:Boolean)
      {
         super(param1,param2,param3);
         if(param3)
         {
            selfBg = BobRendererContainer(param1).selfBgsEnemy[param2];
         }
      }
      
      override public function setData(param1:Object) : void
      {
         super.setData(param1);
         if(this.isBlogger)
         {
            this.setBloggerBG();
         }
      }
      
      override protected function setSelfBG() : void
      {
         if(selfBg != null)
         {
            selfBg.visible = this.isBlogger || UserTags.isCurrentPlayer(model.userTags);
            if(selfBg.visible)
            {
               if(this.isBlogger)
               {
                  this.setBloggerBG();
               }
               else
               {
                  selfBg.source = RES_ICONS.MAPS_ICONS_BATTLELOADING_BOBSELFBG;
               }
            }
         }
      }
      
      private function setBloggerBG() : void
      {
         var _loc1_:String = null;
         if(selfBg)
         {
            selfBg.source = RES_ICONS.MAPS_ICONS_BATTLELOADING_BLOGGER;
            _loc1_ = BLOGGER_COLOR_SCHEME_PREFIX + this.bloggerID;
            selfBg.transform.colorTransform = App.colorSchemeMgr.getTransform(_loc1_);
         }
      }
      
      private function get isBlogger() : Boolean
      {
         return BobDAAPIVehicleInfoVO(model).isBlogger;
      }
      
      private function get bloggerID() : int
      {
         return BobDAAPIVehicleInfoVO(model).bloggerID;
      }
   }
}
