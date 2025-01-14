package net.wg.gui.lobby.battleResults.commendation
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.generated.PLAYER_SATISFACTION_RATING;
   import net.wg.gui.components.containers.HorizontalGroupLayout;
   import net.wg.infrastructure.base.meta.IPlayerSatisfactionWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.PlayerSatisfactionWidgetMeta;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.data.DataProvider;
   
   public class PlayerSatisfactionWidget extends PlayerSatisfactionWidgetMeta implements IPlayerSatisfactionWidgetMeta
   {
      
      private static const _BTN_LINKAGE:String = "CommendationButtonUI";
      
      private static const _BTN_GROUP_PADDING_RIGHT:int = 10;
      
      private static const _BTNS_GAP:int = 2;
       
      
      public var text:TextField;
      
      public var highlightBg:CommendationBgMC;
      
      private var _feedbackStrings:Object;
      
      private var _pageButtons:CommendationButtonGroupContainer;
      
      public function PlayerSatisfactionWidget()
      {
         this._pageButtons = new CommendationButtonGroupContainer();
         super();
      }
      
      override protected function setInitData(param1:Array, param2:Array, param3:int) : void
      {
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc4_:DataProvider = new DataProvider();
         this._feedbackStrings = new Object();
         var _loc7_:int = 0;
         while(_loc7_ < param1.length)
         {
            this._feedbackStrings[param1[_loc7_]] = param2[_loc7_];
            if(param1[_loc7_] != PLAYER_SATISFACTION_RATING.NONE)
            {
               if(param1[_loc7_] == PLAYER_SATISFACTION_RATING.WORSE)
               {
                  _loc5_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_NEGATIVE;
                  _loc6_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_NEGATIVE_GLOW;
               }
               else if(param1[_loc7_] == PLAYER_SATISFACTION_RATING.USUAL)
               {
                  _loc5_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_NEUTRAL;
                  _loc6_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_NEUTRAL_GLOW;
               }
               else if(param1[_loc7_] == PLAYER_SATISFACTION_RATING.BETTER)
               {
                  _loc5_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_POSITIVE;
                  _loc6_ = RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_POSITIVE_GLOW;
               }
               _loc4_.push(new CommendationBtnData(_loc5_,RES_ICONS.MAPS_ICONS_COMMENDATIONS_CHOICE_DEFAULT_GLOW,_loc6_,param1[_loc7_]));
            }
            _loc7_++;
         }
         this._pageButtons.dataProvider = _loc4_;
         this._pageButtons.selectedID = param3;
         this.applySelectionUI(param3);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this._pageButtons.x = width - this._pageButtons.width - _BTN_GROUP_PADDING_RIGHT;
            this._pageButtons.y = height - this._pageButtons.height >> 1;
         }
      }
      
      public function destroy() : void
      {
         dispatchEvent(new PlayerSatisfactionWidgetEvent(PlayerSatisfactionWidgetEvent.DESTROYED,true));
         dispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         dispatchEvent(new PlayerSatisfactionWidgetEvent(PlayerSatisfactionWidgetEvent.CREATED,true));
         addChild(this._pageButtons);
         var _loc1_:HorizontalGroupLayout = new HorizontalGroupLayout();
         _loc1_.gap = _BTNS_GAP;
         this._pageButtons.layout = _loc1_;
         this._pageButtons.itemRendererLinkage = _BTN_LINKAGE;
         this._pageButtons.addEventListener(Event.RESIZE,this.onButtonGroupResizeHandler);
         this._pageButtons.addEventListener(CBGEvent.BTN_CLICKED,this.onButtonGroupChangeHandler);
         this._pageButtons.addEventListener(MouseEvent.MOUSE_OVER,this.onCmpMouseOver);
         this._pageButtons.highlightButtons = [PLAYER_SATISFACTION_RATING.USUAL];
      }
      
      override protected function onDispose() : void
      {
         this._pageButtons.removeEventListener(Event.RESIZE,this.onButtonGroupResizeHandler);
         this._pageButtons.removeEventListener(CBGEvent.BTN_CLICKED,this.onButtonGroupChangeHandler);
         this._pageButtons.removeEventListener(MouseEvent.MOUSE_OVER,this.onCmpMouseOver);
         this._pageButtons = null;
         super.onDispose();
      }
      
      private function onButtonGroupChangeHandler(param1:CBGEvent) : void
      {
         var _loc2_:int = param1.btnID;
         this.applySelectionUI(_loc2_);
         selectedChoiceS(_loc2_);
      }
      
      private function applySelectionUI(param1:int) : void
      {
         var _loc2_:TextFormat = this.text.getTextFormat();
         _loc2_.color = 9211006;
         if(param1 == PLAYER_SATISFACTION_RATING.WORSE)
         {
            this.highlightBg.switchState3();
            _loc2_.color = 12559251;
         }
         else if(param1 == PLAYER_SATISFACTION_RATING.USUAL)
         {
            this.highlightBg.switchState2();
            _loc2_.color = 8290945;
         }
         else if(param1 == PLAYER_SATISFACTION_RATING.BETTER)
         {
            this.highlightBg.switchState1();
            _loc2_.color = 10593672;
         }
         else
         {
            this.highlightBg.switchDefault();
         }
         var _loc3_:String = "";
         if(param1 in this._feedbackStrings)
         {
            _loc3_ = this._feedbackStrings[param1];
         }
         this.text.text = _loc3_;
         this.text.setTextFormat(_loc2_);
         this.text.y = height - this.text.height >> 1;
      }
      
      private function onButtonGroupResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
      
      private function onCmpMouseOver(param1:MouseEvent) : void
      {
         this._pageButtons.removeEventListener(MouseEvent.MOUSE_OVER,this.onCmpMouseOver);
         if(this._pageButtons.highlightButtons && this._pageButtons.highlightButtons.length > 0)
         {
            this._pageButtons.highlightButtons = [];
         }
      }
   }
}
