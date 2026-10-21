package net.wg.portal.gui.battle.fullStats.components
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.portal.data.VO.fullStats.PortalFullStatsVO;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   
   public class ScoreBlock extends SimpleDisposable
   {
      
      private static const SEPARATOR:String = " / ";
      
      private static const COUNTER_TEXT_SIZE_EXTRA_SMALL:uint = 28;
      
      private static const COUNTER_TEXT_SIZE_LARGE:uint = 48;
      
      private static const COUNTER_TEXT_SIZE_EXTRA_LARGE:uint = 56;
      
      private static const LABEL_TEXT_SIZE_EXTRA_SMALL:uint = 20;
      
      private static const LABEL_TEXT_SIZE_LARGE:uint = 28;
      
      private static const LABEL_TEXT_SIZE_EXTRA_LARGE:uint = 36;
      
      private static const LABEL_TF_PADDING_RIGHT_EXTRA_SMALL:uint = 16;
      
      private static const LABEL_TF_PADDING_RIGHT_LARGE:uint = 20;
      
      private static const LABEL_TF_PADDING_RIGHT_EXTRA_LARGE:uint = 28;
      
      private static const SEPARATOR_Y_EXTRA_SMALL:uint = 39;
      
      private static const SEPARATOR_Y_LARGE:uint = 68;
      
      private static const SEPARATOR_Y_EXTRA_LARGE:uint = 74;
       
      
      public var counterTf:TextField = null;
      
      public var labelTf:TextField = null;
      
      public var separator:Sprite = null;
      
      private var _counterTfFormat:TextFormat;
      
      private var _labelTfFormat:TextFormat;
      
      public function ScoreBlock()
      {
         this._counterTfFormat = new TextFormat();
         this._labelTfFormat = new TextFormat();
         super();
         this.counterTf.autoSize = TextFieldAutoSize.CENTER;
         this.labelTf.autoSize = TextFieldAutoSize.LEFT;
         this.labelTf.text = PORTAL_EVENT.BATTLE_TAB_ACTIVECAMPS;
      }
      
      override protected function onDispose() : void
      {
         this.counterTf = null;
         this.labelTf = null;
         this.separator = null;
         this._counterTfFormat = null;
         this._labelTfFormat = null;
         super.onDispose();
      }
      
      public function setData(param1:PortalFullStatsVO) : void
      {
         this.updateCounterTfText(param1.capturedCamps,param1.campsCount);
      }
      
      public function update(param1:int, param2:int) : void
      {
         this.updateCounterTfText(param1,param2);
      }
      
      public function updateStageSize(param1:Number, param2:Number) : void
      {
         var _loc3_:StageBreakPoint = App.stageSizeMgr.currentBreakPoint;
         this._counterTfFormat.size = this.getCounterTextSize(_loc3_);
         this._labelTfFormat.size = this.getLabelTextSize(_loc3_);
         this.counterTf.defaultTextFormat = this._counterTfFormat;
         this.counterTf.setTextFormat(this._counterTfFormat);
         this.labelTf.defaultTextFormat = this._labelTfFormat;
         this.labelTf.setTextFormat(this._labelTfFormat);
         App.utils.commons.updateTextFieldSize(this.counterTf,true,true);
         App.utils.commons.updateTextFieldSize(this.labelTf,true,true);
         this.counterTf.x = 0;
         this.labelTf.x = this.counterTf.textWidth + this.getLabelTfPaddinRightSize(_loc3_) | 0;
         this.labelTf.y = this.counterTf.y + this.counterTf.textHeight - this.labelTf.textHeight | 0;
         this.separator.y = this.getSeparatorY(_loc3_);
         this.separator.width = this.labelTf.x + this.labelTf.textWidth | 0;
      }
      
      private function updateCounterTfText(param1:int, param2:int) : void
      {
         this.counterTf.text = param1 + SEPARATOR + param2;
      }
      
      private function getCounterTextSize(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return COUNTER_TEXT_SIZE_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return COUNTER_TEXT_SIZE_EXTRA_SMALL;
            case StageBreakPointList.LARGE:
               return COUNTER_TEXT_SIZE_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return COUNTER_TEXT_SIZE_EXTRA_LARGE;
            default:
               return COUNTER_TEXT_SIZE_EXTRA_SMALL;
         }
      }
      
      private function getLabelTextSize(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return LABEL_TEXT_SIZE_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return LABEL_TEXT_SIZE_EXTRA_SMALL;
            case StageBreakPointList.LARGE:
               return LABEL_TEXT_SIZE_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return LABEL_TEXT_SIZE_EXTRA_LARGE;
            default:
               return LABEL_TEXT_SIZE_EXTRA_SMALL;
         }
      }
      
      private function getLabelTfPaddinRightSize(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return LABEL_TF_PADDING_RIGHT_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return LABEL_TF_PADDING_RIGHT_EXTRA_SMALL;
            case StageBreakPointList.LARGE:
               return LABEL_TF_PADDING_RIGHT_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return LABEL_TF_PADDING_RIGHT_EXTRA_LARGE;
            default:
               return LABEL_TF_PADDING_RIGHT_EXTRA_SMALL;
         }
      }
      
      private function getSeparatorY(param1:StageBreakPoint) : uint
      {
         switch(param1)
         {
            case StageBreakPointList.SMALL:
               return SEPARATOR_Y_EXTRA_SMALL;
            case StageBreakPointList.MEDIUM:
               return SEPARATOR_Y_EXTRA_SMALL;
            case StageBreakPointList.LARGE:
               return SEPARATOR_Y_LARGE;
            case StageBreakPointList.EXTRA_LARGE:
               return SEPARATOR_Y_EXTRA_LARGE;
            default:
               return SEPARATOR_Y_EXTRA_SMALL;
         }
      }
   }
}
