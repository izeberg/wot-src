package net.wg.gui.components.tooltips
{
   import flash.text.TextField;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.tooltips.VO.TooltipEnvironmentVO;
   import net.wg.gui.events.UILoaderEvent;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class TooltipEnvironment extends ToolTipSpecial
   {
      
      private static const TITLE_ICON_GAP:int = 3;
      
      private static const TITLE_TEXT_GAP:int = 1;
      
      private static const ICON_TEXT_GAP:int = 12;
      
      private static const CONTENT_WIDTH:int = 320;
       
      
      public var titleTF:TextField;
      
      public var textTF:TextField;
      
      public var icon:UILoaderAlt;
      
      public function TooltipEnvironment()
      {
         super();
         this.titleTF = content.titleTF;
         this.textTF = content.textTF;
         this.icon = content.icon;
         this.icon.autoSize = false;
      }
      
      override protected function initData(param1:Object) : void
      {
         super.initData(param1);
         var _loc2_:TooltipEnvironmentVO = new TooltipEnvironmentVO(_data);
         this.titleTF.text = _loc2_.title;
         this.textTF.text = _loc2_.text;
         var _loc3_:String = _loc2_.icon;
         var _loc4_:Boolean = StringUtils.isNotEmpty(_loc3_);
         this.icon.visible = _loc4_;
         if(_loc4_)
         {
            this.icon.addEventListener(UILoaderEvent.COMPLETE,this.onIconCompleteHandler);
            this.icon.source = _loc3_;
         }
         _loc2_.dispose();
      }
      
      override protected function redraw() : void
      {
         var _loc2_:Boolean = false;
         var _loc3_:int = 0;
         var _loc1_:int = contentMargin.left + bgShadowMargin.left;
         topPosition = bgShadowMargin.top + contentMargin.top;
         App.utils.commons.updateTextFieldSize(this.titleTF,true,true);
         this.titleTF.y = topPosition | 0;
         topPosition += this.titleTF.height;
         if(this.icon.visible)
         {
            topPosition += TITLE_ICON_GAP;
            _loc2_ = this.icon.width < CONTENT_WIDTH;
            _loc3_ = Math.max(this.icon.width,CONTENT_WIDTH);
            if(_loc2_)
            {
               this.icon.x = _loc1_ + (_loc3_ - this.icon.width >> 1);
            }
            else
            {
               this.icon.x = _loc1_;
            }
            this.icon.y = topPosition | 0;
            topPosition += this.icon.height + ICON_TEXT_GAP;
            this.textTF.width = _loc3_;
         }
         else
         {
            topPosition += TITLE_TEXT_GAP;
            this.textTF.width = CONTENT_WIDTH;
         }
         this.titleTF.x = _loc1_;
         this.textTF.x = _loc1_;
         this.textTF.y = topPosition | 0;
         App.utils.commons.updateTextFieldSize(this.textTF,false,true);
         super.redraw();
      }
      
      override protected function onDispose() : void
      {
         this.icon.removeEventListener(UILoaderEvent.COMPLETE,this.onIconCompleteHandler);
         this.icon.dispose();
         this.titleTF = null;
         this.textTF = null;
         this.icon = null;
         super.onDispose();
      }
      
      override protected function updateSize() : void
      {
         var _loc1_:int = 0;
         if(this.icon.visible)
         {
            _loc1_ = Math.max(this.icon.width,CONTENT_WIDTH);
         }
         else
         {
            _loc1_ = CONTENT_WIDTH;
         }
         background.width = _loc1_ + contentMargin.horizontal + bgShadowMargin.horizontal | 0;
         background.height = content.height + contentMargin.vertical + bgShadowMargin.vertical | 0;
      }
      
      private function onIconCompleteHandler(param1:UILoaderEvent) : void
      {
         this.redraw();
      }
   }
}
