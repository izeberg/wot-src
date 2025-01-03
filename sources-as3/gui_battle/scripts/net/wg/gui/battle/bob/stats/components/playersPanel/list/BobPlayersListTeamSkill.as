package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.motion.Tween;
   
   public class BobPlayersListTeamSkill extends MovieClip implements IDisposable
   {
      
      private static const NORMAL_LABEL:String = "normal";
      
      private static const HOVER_LABEL:String = "hover";
      
      private static const DEFAULT_ICON_NAME:String = "default";
      
      private static const DEFAULT_TEXT_ALPHA:Number = 0.5;
      
      private static const HEIGHT:int = 60;
      
      private static const LABEL_FADE_OUT_DURATION:int = 500;
       
      
      public var icon:BattleAtlasSprite = null;
      
      public var label:MovieClip = null;
      
      private var _tf:TextField = null;
      
      private var _tween:Tween = null;
      
      private var _tooltipMgr:ITooltipMgr;
      
      private var _initialized:Boolean = false;
      
      private var _collapsed:Boolean = false;
      
      private var _tooltip:String = "";
      
      private var _disposed:Boolean = false;
      
      public function BobPlayersListTeamSkill()
      {
         this._tooltipMgr = App.toolTipMgr;
         super();
      }
      
      public final function dispose() : void
      {
         removeEventListener(MouseEvent.MOUSE_OVER,this.onMouseOver);
         removeEventListener(MouseEvent.MOUSE_OUT,this.onMouseOut);
         this.clearTween();
         this._tf = null;
         this._tooltipMgr = null;
         this.icon = null;
         this.label = null;
         this._disposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function initialize() : void
      {
         if(this._initialized)
         {
            return;
         }
         this._initialized = true;
         this._tf = this.label.tf;
         this._tf.autoSize = TextFieldAutoSize.LEFT;
         this.changeState(NORMAL_LABEL);
         addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOver);
         addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOut);
      }
      
      public function update(param1:String, param2:String, param3:String) : void
      {
         if(param1 == DEFAULT_ICON_NAME)
         {
            this._tooltip = App.toolTipMgr.getNewFormatter().addBody(param3).make();
         }
         else
         {
            this._tooltip = App.toolTipMgr.getNewFormatter().addHeader(param2).addBody(param3).make();
         }
         this._tf.text = param2;
         this._tf.y = HEIGHT - this._tf.height >> 1;
         this._tf.alpha = param1 == DEFAULT_ICON_NAME ? Number(DEFAULT_TEXT_ALPHA) : Number(1);
         this.icon.imageName = param1;
      }
      
      public function collapse() : void
      {
         this.clearTween();
         this._tween = new Tween(LABEL_FADE_OUT_DURATION,this.label,{"alpha":0},{
            "paused":false,
            "ease":Cubic.easeInOut,
            "onComplete":this.onCollapsed
         });
         this._tween.fastTransform = false;
      }
      
      private function onCollapsed() : void
      {
         this.label.visible = false;
         this._collapsed = true;
      }
      
      private function onMouseOver(param1:MouseEvent) : void
      {
         this.changeState(HOVER_LABEL);
         if(this._collapsed)
         {
            this._tooltipMgr.showComplex(this._tooltip);
         }
      }
      
      private function onMouseOut(param1:MouseEvent) : void
      {
         this.changeState(NORMAL_LABEL);
         this._tooltipMgr.hide();
      }
      
      private function changeState(param1:String) : void
      {
         this.gotoAndStop(param1);
         this.label.gotoAndStop(param1);
      }
      
      private function clearTween() : void
      {
         if(this._tween)
         {
            this._tween.dispose();
            this._tween = null;
         }
      }
   }
}
