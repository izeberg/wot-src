package net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components
{
   import flash.text.TextFormat;
   import net.wg.gui.battle.views.gameMessagesPanel.components.EndGameMessageTextfields;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   
   public class HBEndGameMessageTextfields extends EndGameMessageTextfields
   {
      
      private static const TITLE_FONT_SIZE_EXTRA_LARGE:uint = 144;
      
      private static const TITLE_FONT_SIZE:uint = 75;
      
      private static const TITLE_FONT_SIZE_SMALL:uint = 56;
      
      private static const SUBTITLE_FONT_SIZE_EXTRA_LARGE:uint = 28;
      
      private static const SUBTITLE_FONT_SIZE:uint = 16;
      
      private static const SUBTITLE_Y_EXTRA_LARGE:int = 100;
      
      private static const SUBTITLE_Y:int = 43;
      
      private static const SUBTITLE_Y_SMALL:int = 20;
       
      
      private var _titleTf:TextFormat = null;
      
      private var _subTitleTf:TextFormat = null;
      
      public function HBEndGameMessageTextfields()
      {
         super();
         titleTF.cacheAsBitmap = true;
         this._titleTf = titleTF.getTextFormat();
         subtitleTF.cacheAsBitmap = true;
         this._subTitleTf = subtitleTF.getTextFormat();
      }
      
      override protected function onDispose() : void
      {
         this._titleTf = null;
         this._subTitleTf = null;
         super.onDispose();
      }
      
      public function updateLayout(param1:StageBreakPoint) : void
      {
         this._titleTf.size = this.getTitleFontSize(param1);
         titleTF.setTextFormat(this._titleTf);
         App.utils.commons.updateTextFieldSize(titleTF,false,true);
         this._subTitleTf.size = this.getSubTitleFontSize(param1);
         subtitleTF.setTextFormat(this._subTitleTf);
         App.utils.commons.updateTextFieldSize(subtitleTF,false,true);
         subtitleTF.y = this.getSubTitleY(param1);
      }
      
      private function getTitleFontSize(param1:StageBreakPoint) : uint
      {
         if(param1.width < StageBreakPointList.SMALL.width)
         {
            return TITLE_FONT_SIZE_SMALL;
         }
         if(param1 == StageBreakPointList.EXTRA_LARGE)
         {
            return TITLE_FONT_SIZE_EXTRA_LARGE;
         }
         return TITLE_FONT_SIZE;
      }
      
      private function getSubTitleFontSize(param1:StageBreakPoint) : uint
      {
         if(param1 == StageBreakPointList.EXTRA_LARGE)
         {
            return SUBTITLE_FONT_SIZE_EXTRA_LARGE;
         }
         return SUBTITLE_FONT_SIZE;
      }
      
      private function getSubTitleY(param1:StageBreakPoint) : uint
      {
         if(param1.width < StageBreakPointList.SMALL.width)
         {
            return SUBTITLE_Y_SMALL;
         }
         if(param1 == StageBreakPointList.EXTRA_LARGE)
         {
            return SUBTITLE_Y_EXTRA_LARGE;
         }
         return SUBTITLE_Y;
      }
   }
}
