package net.wg.white_tiger.gui.battle.views.wtBattleTimer
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class WTTextFieldContainer extends BattleUIComponent
   {
      
      private static const FRAME_HUNTER:String = "hunter";
      
      private static const FRAME_BOSS:String = "boss";
      
      private static const FRAME_SMALL:String = "_small";
      
      private static const FRAME_BIG:String = "_big";
      
      private static const TEXT_FIELD_BOUNDS_HEIGHT:Number = 4;
       
      
      public var textField:TextField = null;
      
      public var icon:MovieClip = null;
      
      private var _text:String = "";
      
      private var _tf:TextFormat = null;
      
      private var _isBoss:Boolean = false;
      
      private var _isSmall:Boolean = true;
      
      private var _isOvertime:Boolean = false;
      
      public function WTTextFieldContainer()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.icon.visible = false;
         this.textField.cacheAsBitmap = true;
         this._tf = this.textField.getTextFormat();
      }
      
      override protected function onDispose() : void
      {
         this.icon = null;
         this.textField = null;
         this._tf = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         if(StringUtils.isNotEmpty(this._text) && isInvalid(InvalidationType.DATA))
         {
            this.updateData();
         }
      }
      
      private function updateData() : void
      {
         var _loc1_:String = "";
         _loc1_ += !!this._isBoss ? FRAME_BOSS : FRAME_HUNTER;
         _loc1_ += !!this._isSmall ? FRAME_SMALL : FRAME_BIG;
         this.icon.gotoAndStop(_loc1_);
         this.textField.text = this._text;
         App.utils.commons.updateTextFieldSize(this.textField);
         this.textField.height = this.textField.textHeight + TEXT_FIELD_BOUNDS_HEIGHT | 0;
         this.textField.x = -this.textField.width | 0;
         this.textField.y = -this.textField.height >> 1;
         this.icon.x = this.textField.x - (this.icon.width >> 1);
      }
      
      public function set label(param1:String) : void
      {
         if(this._text != param1)
         {
            this._text = param1;
            invalidateData();
         }
      }
      
      public function set fontSize(param1:int) : void
      {
         this._tf.size = param1;
         this.textField.setTextFormat(this._tf);
         invalidateData();
      }
      
      public function set isBoss(param1:Boolean) : void
      {
         if(this._isBoss != param1)
         {
            this._isBoss = param1;
            invalidateData();
         }
      }
      
      public function set isSmall(param1:Boolean) : void
      {
         if(this._isSmall != param1)
         {
            this._isSmall = param1;
            invalidateData();
         }
      }
      
      public function set isOvertime(param1:Boolean) : void
      {
         if(this._isOvertime != param1)
         {
            this._isOvertime = param1;
            this.icon.visible = this._isOvertime;
         }
      }
   }
}
