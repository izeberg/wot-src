package net.wg.gui.lobby.questsWindow.components
{
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.BaseTooltips;
   import net.wg.data.constants.Values;
   import net.wg.data.managers.impl.TooltipProps;
   import net.wg.gui.lobby.questsWindow.data.TextBlockVO;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class QuestTextAwardBlock extends AbstractResizableContent
   {
      
      private static const MAX_TOOLTIP_WIDTH:int = 300;
      
      private static const TEXT_FIELD_PADDING:int = 5;
      
      private static const WARNING_STR:String = "Warn: not one items can be visible. Full items text: ";
       
      
      public var textTf:TextField = null;
      
      protected var _showTooltip:Boolean = true;
      
      private var _tooltip:String = "";
      
      private var _specialTooltipArgs:Array = null;
      
      private var _isTooltipSpecial:Boolean = false;
      
      private var _wulfTooltipArg:String = "";
      
      private var _typedTooltipArg:String = "";
      
      private var _isTooltipComplex:Boolean = false;
      
      private var _isTooltipWulf:Boolean = false;
      
      private var _isTypedTooltip:Boolean = false;
      
      private var _linesLimit:int = -1;
      
      public function QuestTextAwardBlock()
      {
         super();
      }
      
      override public function setData(param1:Object) : void
      {
         var _loc2_:TextBlockVO = new TextBlockVO(param1);
         var _loc3_:Vector.<String> = _loc2_.items;
         var _loc4_:String = _loc2_.separator;
         var _loc5_:String = _loc3_.join(_loc4_) + _loc2_.endline;
         this._linesLimit = _loc2_.linesLimit;
         if(this.calcVisibleItemsLen(_loc3_,_loc5_,_loc2_.ellipsis,_loc4_.length) == 0)
         {
            DebugUtils.LOG_WARNING(WARNING_STR + _loc5_);
         }
         else
         {
            App.utils.commons.updateTextFieldSize(this.textTf,false,true);
            this.updateSize();
            if(this._showTooltip)
            {
               this.textTf.addEventListener(MouseEvent.ROLL_OVER,this.onTextTfRollOverHandler);
               this.textTf.addEventListener(MouseEvent.ROLL_OUT,this.onTextTfRollOutHandler);
               this._isTooltipComplex = StringUtils.isNotEmpty(_loc2_.complexTooltip);
               this._isTooltipSpecial = StringUtils.isNotEmpty(_loc2_.specialTooltip);
               this._isTooltipWulf = StringUtils.isNotEmpty(_loc2_.wulfTooltip);
               this._isTypedTooltip = StringUtils.isNotEmpty(_loc2_.typedTooltip);
               if(this._isTooltipWulf)
               {
                  this._tooltip = _loc2_.wulfTooltip;
                  this._wulfTooltipArg = _loc2_.wulfTooltipArg;
               }
               else if(this._isTooltipSpecial)
               {
                  this._tooltip = _loc2_.specialTooltip;
                  this._specialTooltipArgs = _loc2_.specialTooltipArgs;
               }
               else if(this._isTooltipComplex)
               {
                  this._tooltip = _loc2_.complexTooltip;
               }
               else if(this._isTypedTooltip)
               {
                  this._tooltip = _loc2_.typedTooltip;
                  this._typedTooltipArg = _loc2_.typedTooltipArg;
               }
               else
               {
                  this._tooltip = _loc5_;
               }
            }
         }
         _loc2_.dispose();
      }
      
      override protected function onDispose() : void
      {
         this.textTf.removeEventListener(MouseEvent.ROLL_OVER,this.onTextTfRollOverHandler);
         this.textTf.removeEventListener(MouseEvent.ROLL_OUT,this.onTextTfRollOutHandler);
         this.textTf = null;
         if(this._specialTooltipArgs != null)
         {
            this._specialTooltipArgs.splice(0,this._specialTooltipArgs.length);
            this._specialTooltipArgs = null;
         }
         super.onDispose();
      }
      
      protected function updateSize() : void
      {
         setSize(width,actualHeight);
      }
      
      protected function calcVisibleItemsLen(param1:Vector.<String>, param2:String, param3:String, param4:int) : int
      {
         var _loc7_:int = 0;
         var _loc5_:Number = this.textTf.height;
         var _loc6_:int = param1.length;
         this.textTf.htmlText = param2;
         if(!this.fixedMode || !this.lineLimit)
         {
            while(this.textTf.textHeight + TEXT_FIELD_PADDING > _loc5_)
            {
               this.textTf.htmlText = param2.substr(0,this.getItemsStringLen(param1,--_loc6_,param4)) + param3;
               this._showTooltip = true;
            }
         }
         else
         {
            _loc7_ = this.textTf.length;
            App.utils.commons.truncateHtmlTextMultiline(this.textTf,param2,this.lineLimit,this.lineEnd);
            this._showTooltip = _loc7_ != this.textTf.length;
         }
         return _loc6_;
      }
      
      private function getItemsStringLen(param1:Vector.<String>, param2:int, param3:int) : int
      {
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         while(_loc5_ < param2)
         {
            _loc4_ += param1[_loc5_].length + param3;
            _loc5_++;
         }
         return _loc4_;
      }
      
      protected function get fixedMode() : Boolean
      {
         return false;
      }
      
      protected function get lineLimit() : int
      {
         return this._linesLimit;
      }
      
      protected function get lineEnd() : String
      {
         return Values.EMPTY_STR;
      }
      
      private function onTextTfRollOverHandler(param1:MouseEvent) : void
      {
         if(this._showTooltip)
         {
            if(this._isTooltipWulf)
            {
               App.toolTipMgr.showWulfTooltip(this._tooltip,this._wulfTooltipArg);
            }
            else if(this._isTooltipComplex)
            {
               App.toolTipMgr.showComplex(this._tooltip);
            }
            else if(this._isTypedTooltip)
            {
               App.toolTipMgr.showSpecial(this._tooltip,null,this._typedTooltipArg);
            }
            else
            {
               App.toolTipMgr.show(this._tooltip,new TooltipProps(BaseTooltips.TYPE_INFO,0,0,0,-1,0,MAX_TOOLTIP_WIDTH));
            }
         }
      }
      
      private function onTextTfRollOutHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.hide();
      }
   }
}
