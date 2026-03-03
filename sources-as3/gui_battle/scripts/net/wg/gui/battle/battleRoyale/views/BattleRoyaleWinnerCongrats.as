package net.wg.gui.battle.battleRoyale.views
{
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.battleRoyale.views.components.BattleRoyaleWinnerCongratsAnimation;
   import net.wg.gui.battle.battleRoyale.views.shamrock.components.results.WinnerShamrockAnimation;
   import net.wg.infrastructure.base.meta.IBattleRoyaleWinnerCongratsMeta;
   import net.wg.infrastructure.base.meta.impl.BattleRoyaleWinnerCongratsMeta;
   import net.wg.utils.IClassFactory;
   
   public class BattleRoyaleWinnerCongrats extends BattleRoyaleWinnerCongratsMeta implements IBattleRoyaleWinnerCongratsMeta
   {
      
      private static const FRAME_START:int = 1;
      
      private static const VERTICAL_ALIGNMENT_PERCENT:Number = 0.3;
      
      private static const ANIMATION_UI:String = "BRWinnerCongratsAnimationUI";
      
      private static const VIGNETTE_MC:String = "BRWinnerCongratsVignetteMC";
      
      private static const GRADIENT_MC:String = "BRWinnerCongratsGradientMC";
      
      private static const SHAMROCK_ANIMATION_MC:String = "BRWinnerShamrockAnimationUI";
      
      private static const SHAMROCK_ANIMATION_Y_OFFSET:int = 210;
       
      
      public var animation:BattleRoyaleWinnerCongratsAnimation = null;
      
      public var vignette:MovieClip = null;
      
      public var gradient:MovieClip = null;
      
      public var shamrockAnimation:WinnerShamrockAnimation = null;
      
      private var _classFactory:IClassFactory = null;
      
      private var _stageWidth:int = 0;
      
      private var _stageHeight:int = 0;
      
      private var _isInitialized:Boolean = false;
      
      public function BattleRoyaleWinnerCongrats()
      {
         super();
         this.setCompVisible(false);
         this._classFactory = App.instance.utils.classFactory;
      }
      
      override public function setCompVisible(param1:Boolean) : void
      {
         super.setCompVisible(param1);
         if(param1)
         {
            if(!this._isInitialized)
            {
               this.initContent();
            }
            this.animation.gotoAndPlay(FRAME_START);
            this.vignette.gotoAndPlay(FRAME_START);
            this.gradient.gotoAndPlay(FRAME_START);
            this.shamrockAnimation.gotoAndPlay(FRAME_START);
            playWinSoundS();
         }
         else if(this._isInitialized)
         {
            this.animation.stop();
            this.vignette.stop();
            this.gradient.stop();
            this.shamrockAnimation.stop();
         }
      }
      
      override protected function onDispose() : void
      {
         this.gradient = null;
         this.vignette = null;
         if(this._isInitialized)
         {
            this.animation.dispose();
            this.animation = null;
         }
         if(this.shamrockAnimation)
         {
            this.shamrockAnimation.dispose();
            this.shamrockAnimation = null;
         }
         this._isInitialized = false;
         this._classFactory = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._isInitialized && isInvalid(InvalidationType.SIZE))
         {
            this.gradient.x = this.vignette.x = 0;
            this.gradient.y = this.vignette.y = 0;
            this.gradient.width = this.vignette.width = this._stageWidth;
            this.gradient.height = this.vignette.height = this._stageHeight;
            this.animation.x = this._stageWidth >> 1;
            this.animation.y = this._stageHeight * VERTICAL_ALIGNMENT_PERCENT >> 0;
            this.shamrockAnimation.x = this._stageWidth >> 1;
            this.shamrockAnimation.y = this.animation.y + SHAMROCK_ANIMATION_Y_OFFSET;
         }
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         this._stageWidth = param1;
         this._stageHeight = param2;
         invalidateSize();
      }
      
      private function initContent() : void
      {
         if(this._classFactory)
         {
            this.animation = this._classFactory.getComponent(ANIMATION_UI,BattleRoyaleWinnerCongratsAnimation);
            this.vignette = this._classFactory.getComponent(VIGNETTE_MC,MovieClip);
            this.gradient = this._classFactory.getComponent(GRADIENT_MC,MovieClip);
            this.shamrockAnimation = this._classFactory.getComponent(SHAMROCK_ANIMATION_MC,WinnerShamrockAnimation);
            addChild(this.animation);
            addChild(this.vignette);
            addChild(this.gradient);
            addChild(this.shamrockAnimation);
            invalidateSize();
            this._isInitialized = true;
         }
      }
      
      public function as_setStpCoins(param1:int, param2:int, param3:int) : void
      {
         if(this.shamrockAnimation)
         {
            this.shamrockAnimation.setValues(param1,param2,param3);
         }
      }
   }
}
