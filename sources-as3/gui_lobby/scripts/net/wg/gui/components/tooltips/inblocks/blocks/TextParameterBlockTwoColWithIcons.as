package net.wg.gui.components.tooltips.inblocks.blocks
{
   import flash.events.Event;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.tooltips.inblocks.data.TextParameterTwoColWithIconsVO;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class TextParameterBlockTwoColWithIcons extends TextParameterBlockTwoCol
   {
       
      
      public var icon:Image = null;
      
      public var icon2:Image = null;
      
      public function TextParameterBlockTwoColWithIcons()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.icon.removeEventListener(Event.CHANGE,this.onImageChangeHandler);
         this.icon.dispose();
         this.icon = null;
         this.icon2.removeEventListener(Event.CHANGE,this.onImageChangeHandler);
         this.icon2.dispose();
         this.icon2 = null;
         super.onDispose();
      }
      
      override public function cleanUp() : void
      {
         this.icon.x = this.icon.y = 0;
         this.icon.source = null;
         this.icon2.x = this.icon2.y = 0;
         this.icon2.source = null;
         super.cleanUp();
      }
      
      override protected function getDataClass() : Class
      {
         return TextParameterTwoColWithIconsVO;
      }
      
      override protected function applyParamValue() : void
      {
         super.applyParamValue();
         var _loc1_:TextParameterTwoColWithIconsVO = _data as TextParameterTwoColWithIconsVO;
         if(!_loc1_)
         {
            return;
         }
         this.icon.visible = StringUtils.isNotEmpty(_loc1_.icon);
         if(this.icon.visible)
         {
            this.icon.source = _loc1_.icon;
            this.icon.addEventListener(Event.CHANGE,this.onImageChangeHandler);
         }
         this.icon2.visible = StringUtils.isNotEmpty(_loc1_.icon2);
         if(this.icon2.visible)
         {
            this.icon2.source = _loc1_.icon2;
            this.icon2.addEventListener(Event.CHANGE,this.onImageChangeHandler);
         }
         this.invalidateIcons();
      }
      
      private function invalidateIcons() : void
      {
         var _loc1_:TextParameterTwoColWithIconsVO = null;
         _loc1_ = _data as TextParameterTwoColWithIconsVO;
         if(!_loc1_)
         {
            return;
         }
         if(this.icon.ready && this.icon.visible)
         {
            this.icon.x = valueTF.x + valueTF.width - valueTF.textWidth - this.icon.width | 0;
            this.icon.y = 0;
            if(_loc1_.iconPadding != null)
            {
               this.icon.x += _loc1_.iconPadding.left - _loc1_.iconPadding.right;
               this.icon.y += _loc1_.iconPadding.top - _loc1_.iconPadding.bottom;
            }
         }
         if(this.icon2.ready && this.icon2.visible)
         {
            this.icon2.x = value2TF.x + value2TF.width - value2TF.textWidth - this.icon2.width | 0;
            this.icon2.y = 0;
            if(_loc1_.iconPadding != null)
            {
               this.icon2.x += _loc1_.iconPadding.left - _loc1_.iconPadding.right;
               this.icon2.y += _loc1_.iconPadding.top - _loc1_.iconPadding.bottom;
            }
         }
      }
      
      private function onImageChangeHandler(param1:Event) : void
      {
         this.invalidateIcons();
      }
   }
}
