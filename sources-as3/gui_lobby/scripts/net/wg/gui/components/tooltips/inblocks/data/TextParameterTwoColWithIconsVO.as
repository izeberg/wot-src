package net.wg.gui.components.tooltips.inblocks.data
{
   import net.wg.data.VO.PaddingVO;
   
   public class TextParameterTwoColWithIconsVO extends TextParameterTwoColVO
   {
      
      private static const ICON_PADDING_FIELD_NAME:String = "iconPadding";
       
      
      public var icon:String = "";
      
      public var icon2:String = "";
      
      public var iconPadding:PaddingVO = null;
      
      public function TextParameterTwoColWithIconsVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == ICON_PADDING_FIELD_NAME && param2 != null)
         {
            this.iconPadding = new PaddingVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.iconPadding != null)
         {
            this.iconPadding.dispose();
            this.iconPadding = null;
         }
         super.onDispose();
      }
   }
}
