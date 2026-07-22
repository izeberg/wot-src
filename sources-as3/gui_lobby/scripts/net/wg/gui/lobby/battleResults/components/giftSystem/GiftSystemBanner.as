package net.wg.gui.lobby.battleResults.components.giftSystem
{
   import flash.text.TextField;
   import net.wg.gui.lobby.battleResults.data.GiftSystemVO;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class GiftSystemBanner extends UIComponentEx
   {
      
      private static const STAMPS_RIGHT_OFFSET:uint = 7;
       
      
      public var stamps:GiftSystemStamps = null;
      
      public var title:TextField = null;
      
      private var _data:GiftSystemVO = null;
      
      public function GiftSystemBanner()
      {
         super();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.title.htmlText = this._data.bannerTitle;
            this.stamps.x = this.width - this.stamps.width - STAMPS_RIGHT_OFFSET;
         }
      }
      
      override protected function onDispose() : void
      {
         this.stamps.dispose();
         this.stamps = null;
         this.title = null;
         this._data = null;
         super.onDispose();
      }
      
      public function updateData(param1:GiftSystemVO) : void
      {
         this._data = param1;
         this.stamps.updateData(param1.stamp);
         invalidateData();
      }
   }
}
