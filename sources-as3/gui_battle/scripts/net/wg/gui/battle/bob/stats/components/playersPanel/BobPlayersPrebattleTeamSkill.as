package net.wg.gui.battle.bob.stats.components.playersPanel
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class BobPlayersPrebattleTeamSkill extends Sprite implements IDisposable
   {
      
      private static const NO_SKILL_ICON_NAME:String = "default";
      
      private static const DESCRIPTION_TOP_GAP:int = -1;
      
      private static const LABEL_FADE_OUT_DURATION:int = 500;
      
      private static const LABEL_FADE_OUT_Y_OFFSET:int = 15;
       
      
      public var icon:BattleAtlasSprite = null;
      
      public var textFields:MovieClip = null;
      
      private var _title:TextField = null;
      
      private var _description:TextField = null;
      
      private var _tween:Tween = null;
      
      private var _initialized:Boolean = false;
      
      private var _disposed:Boolean = false;
      
      public function BobPlayersPrebattleTeamSkill()
      {
         super();
      }
      
      public function initialize() : void
      {
         if(this._initialized)
         {
            return;
         }
         this._initialized = true;
         this._title = this.textFields.title;
         this._description = this.textFields.description;
         this._title.autoSize = TextFieldAutoSize.LEFT;
         this._description.autoSize = TextFieldAutoSize.LEFT;
      }
      
      public final function dispose() : void
      {
         this.clearTween();
         this._title = null;
         this._description = null;
         this.icon = null;
         this.textFields = null;
         this._disposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function update(param1:String, param2:String, param3:String) : void
      {
         if(param1 == NO_SKILL_ICON_NAME)
         {
            this.hide(true);
         }
         else
         {
            this.icon.imageName = param1;
            this._title.text = param2;
            this._description.text = param3;
            this.updateLayout();
         }
      }
      
      public function hide(param1:Boolean = false) : void
      {
         if(param1)
         {
            visible = false;
         }
         else
         {
            this.clearTween();
            this._tween = new Tween(LABEL_FADE_OUT_DURATION,this,{
               "alpha":0,
               "y":this.y + LABEL_FADE_OUT_Y_OFFSET
            },{
               "paused":false,
               "ease":Cubic.easeInOut,
               "onComplete":this.onHideTweenComplete
            });
            this._tween.fastTransform = false;
         }
      }
      
      private function onHideTweenComplete() : void
      {
         visible = false;
      }
      
      private function clearTween() : void
      {
         if(this._tween)
         {
            this._tween.dispose();
            this._tween = null;
         }
      }
      
      private function updateLayout() : void
      {
         this._description.y = this._title.height + this._title.y + DESCRIPTION_TOP_GAP >> 0;
      }
   }
}
