package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.geom.Point;
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.actionMarkers.ActionMarkerStates;
   import net.wg.gui.battle.views.actionMarkers.BaseActionMarker;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class VehicleActionMarker extends BaseActionMarker implements IDisposable
   {
      
      private static const BASE_WIDTH:int = 20;
      
      private static const BASE_HEIGHT:int = 20;
      
      private static const ACTION_RENDERER_MAP:Object = {
         "reloading_gun":VehicleMarkersLinkages.ACTION_RELOADING,
         "help_me":VehicleMarkersLinkages.ACTION_HELP_ME,
         "attackSender":VehicleMarkersLinkages.ACTION_ATTACK_SENDER,
         "positive":VehicleMarkersLinkages.ACTION_POSITIVE,
         "thanks":VehicleMarkersLinkages.ACTION_THANKS,
         "help_me_ex":VehicleMarkersLinkages.ACTION_HELP_ME_EX,
         "turn_back":VehicleMarkersLinkages.ACTION_TURN_BACK,
         "supportingAlly":VehicleMarkersLinkages.ACTION_SUPPORTING_ALLY,
         "supportingYou":VehicleMarkersLinkages.ACTION_SUPPORTING_YOU,
         "attack":VehicleMarkersLinkages.ACTION_ATTACK,
         "attackAlternative":VehicleMarkersLinkages.ACTION_ATTACK_ALTERNATIVE,
         "supportingAllyAlternative":VehicleMarkersLinkages.ACTION_SUPPORTING_ALLY_ALTERNATIVE,
         "goingToAlternative":VehicleMarkersLinkages.ACTION_GOING_TO,
         "attackBaseAlternative":VehicleMarkersLinkages.ACTION_ATTACK_BASE,
         "defendBaseAlternative":VehicleMarkersLinkages.ACTION_DEFEND_BASE,
         "attackingBaseAlternative":VehicleMarkersLinkages.ACTION_ATTACK_BASE,
         "defendingBaseAlternative":VehicleMarkersLinkages.ACTION_DEFEND_BASE,
         "attackObjectiveAlternative":VehicleMarkersLinkages.ACTION_ATTACKING_OBJECTIVE,
         "defendObjectiveAlternative":VehicleMarkersLinkages.ACTION_DEFENDING_OBJECTIVE,
         "attackingObjectiveAlternative":VehicleMarkersLinkages.ACTION_ATTACKING_OBJECTIVE,
         "defendingObjectiveAlternative":VehicleMarkersLinkages.ACTION_DEFENDING_OBJECTIVE
      };
      
      private static const ACTION_ICON_STATE:String = "actionIconState";
       
      
      private var _isVisible:Boolean = false;
      
      private var _currentRenderer:ActionAnim = null;
      
      private var _entityName:String = "enemy";
      
      private var _actionJustChanged:Boolean = false;
      
      private var _actionIconStateMarker:ActionIconStateMarker = null;
      
      private var _count:int = 0;
      
      private var _lastState:int = -1;
      
      private var _pyrometer:PyrometerAction = null;
      
      public const ARROW_POSITION:Point = new Point(0,0);
      
      public const REPLY_POSITION:Point = new Point(20,-1);
      
      public const DISTANCE_POSITION:Point = new Point(-43,15);
      
      public function VehicleActionMarker()
      {
         super();
      }
      
      override public function setReplyCount(param1:int) : void
      {
         this._count = param1;
         super.setReplyCount(param1);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.POSITION))
         {
            this.updatePositions();
         }
      }
      
      override protected function onDispose() : void
      {
         this.removeActionRenderer();
         this._currentRenderer = null;
         if(this._actionIconStateMarker != null)
         {
            this._actionIconStateMarker.dispose();
         }
         this._actionIconStateMarker = null;
         if(this._pyrometer)
         {
            this._pyrometer.dispose();
            this._pyrometer = null;
         }
         super.onDispose();
      }
      
      public function hidePyrometer() : void
      {
         if(this._pyrometer)
         {
            this._pyrometer.hideImmediately();
            invalidatePosition();
         }
      }
      
      public function isVisible() : Boolean
      {
         return this._isVisible;
      }
      
      public function showAction(param1:String, param2:Boolean = false) : void
      {
         if(param1 == Values.EMPTY_STR)
         {
            return;
         }
         var _loc3_:String = ACTION_RENDERER_MAP[param1];
         if(_loc3_ != Values.EMPTY_STR)
         {
            this._currentRenderer = this.createActionRenderer(_loc3_);
         }
         this._currentRenderer.show();
         this._isVisible = true;
         this._actionIconStateMarker = ActionIconStateMarker(this._currentRenderer.getChildByName(ACTION_ICON_STATE));
         this._actionJustChanged = true;
         if(param2 && this._lastState != -1)
         {
            this.updateActionRenderer(this._lastState);
         }
         invalidatePosition();
      }
      
      public function showPyrometer(param1:Boolean, param2:int) : void
      {
         if(!this._pyrometer)
         {
            this._pyrometer = PyrometerAction(this.createActionRenderer(VehicleMarkersLinkages.PYROMETER_ACTION));
         }
         this._pyrometer.isAlly = param1;
         this._pyrometer.showByDuration(param2);
         this._isVisible = true;
         invalidatePosition();
      }
      
      public function stopAction(param1:Boolean = true) : void
      {
         if(this._currentRenderer)
         {
            if(param1)
            {
               this._currentRenderer.hideAnim();
            }
            else
            {
               this._currentRenderer.hideImmediately();
            }
            this.updateVisibility();
         }
      }
      
      public function triggerClickAnimation() : void
      {
         if(this._actionIconStateMarker != null)
         {
            this._actionIconStateMarker.playClickAnimation();
         }
      }
      
      public function updateActionRenderer(param1:int) : void
      {
         if(!this._currentRenderer)
         {
            return;
         }
         if(this._actionIconStateMarker != null)
         {
            if(this._actionJustChanged && param1 != ActionMarkerStates.REPLIED_ALLY && param1 != ActionMarkerStates.REPLIED_ME && this._count == 0)
            {
               this._actionIconStateMarker.playBlinkAnimation(true);
            }
            else if(this._count >= 1)
            {
               this._actionIconStateMarker.playBlinkAnimation(false);
            }
            this._actionJustChanged = false;
            this._actionIconStateMarker.gotoAndStop(ActionMarkerStates.STATE_INT_TO_STRING[param1]);
            this._lastState = param1;
         }
      }
      
      private function updatePositions() : void
      {
         if(!this._isVisible)
         {
            return;
         }
         var _loc1_:Vector.<MovieClip> = new Vector.<MovieClip>(0);
         if(this._pyrometer && this._pyrometer.visible)
         {
            _loc1_.push(this._pyrometer);
         }
         if(this._currentRenderer && this._currentRenderer.visible)
         {
            _loc1_.push(this._currentRenderer);
         }
         var _loc2_:int = _loc1_.length;
         var _loc3_:int = _loc2_ > 1 ? int(-_loc2_ * (BASE_WIDTH >> 1) >> 1) : int(0);
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc1_[_loc4_].x = _loc3_;
            _loc3_ += BASE_WIDTH;
            _loc4_++;
         }
      }
      
      private function removeActionRenderer() : void
      {
         if(!this._currentRenderer)
         {
            return;
         }
         removeChild(this._currentRenderer);
         this._currentRenderer.removeEventListener(Event.COMPLETE,this.onHideAnimComplete);
         this._currentRenderer = null;
      }
      
      private function createActionRenderer(param1:String) : ActionAnim
      {
         var rendererClass:Class = null;
         var rendererLinkage:String = param1;
         this.removeActionRenderer();
         var renderer:ActionAnim = null;
         try
         {
            rendererClass = getDefinitionByName(rendererLinkage) as Class;
            renderer = new rendererClass();
            if(renderer)
            {
               addChild(renderer);
               renderer.addEventListener(Event.COMPLETE,this.onHideAnimComplete);
            }
         }
         catch(error:ReferenceError)
         {
         }
         return renderer;
      }
      
      private function onHideAnimComplete() : void
      {
         this.updateVisibility();
         invalidatePosition();
      }
      
      private function updateVisibility() : void
      {
         this._isVisible = this._currentRenderer && this._currentRenderer.visible || this._pyrometer && this._pyrometer.visible;
      }
      
      override protected function get getReplyPosition() : Point
      {
         return this.REPLY_POSITION;
      }
      
      override protected function get getArrowPosition() : Point
      {
         return this.ARROW_POSITION;
      }
      
      override protected function get getDistanceToMarkerPosition() : Point
      {
         return this.DISTANCE_POSITION;
      }
      
      override public function get height() : Number
      {
         return BASE_HEIGHT;
      }
      
      public function updateArrowPosition(param1:Point) : void
      {
         stickyMarker.setArrowPosition(param1);
      }
      
      public function get entityName() : String
      {
         return this._entityName;
      }
      
      public function set entityName(param1:String) : void
      {
         this._entityName = param1;
      }
   }
}
