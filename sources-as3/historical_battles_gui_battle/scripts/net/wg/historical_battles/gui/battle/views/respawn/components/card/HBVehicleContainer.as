package net.wg.historical_battles.gui.battle.views.respawn.components.card
{
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.historical_battles.data.constants.generated.HB_VEHICLE_CARD_STATE;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_VEHICLE_CARD_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBVehicleCardVO;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBVehicleCardEvent;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import net.wg.utils.IClassFactory;
   import scaleform.clik.motion.Tween;
   
   public class HBVehicleContainer extends BattleUIComponent implements IUpdatable
   {
      
      private static const CARD_LINKAGE:String = "HBVehicleCardUI";
      
      private static const TWEEN_DURATION:Number = 300;
       
      
      private var _cards:Vector.<HBVehicleCard>;
      
      private var _data:Vector.<HBVehicleCardVO> = null;
      
      private var _classFactory:IClassFactory;
      
      private var _size:uint = 0;
      
      private var _tweens:Vector.<Tween> = null;
      
      private var _hasAnim:Boolean = false;
      
      public function HBVehicleContainer()
      {
         this._cards = new Vector.<HBVehicleCard>(0);
         this._classFactory = App.utils.classFactory;
         super();
         this._tweens = new Vector.<Tween>(0);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(HBVehicleCardEvent.VEHICLE_PICK,this.onVehiclePickHandler);
      }
      
      override protected function onDispose() : void
      {
         this.clearTweens();
         this._tweens = null;
         removeEventListener(HBVehicleCardEvent.VEHICLE_PICK,this.onVehiclePickHandler);
         this.cleanCards();
         this._cards = null;
         this._data = null;
         this._classFactory = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:HBVehicleCard = null;
         var _loc2_:HBVehicleCardVO = null;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.cleanCards();
               for each(_loc2_ in this._data)
               {
                  _loc1_ = this._classFactory.getComponent(CARD_LINKAGE,HBVehicleCard);
                  _loc1_.update(_loc2_);
                  this._cards.push(_loc1_);
                  addChild(_loc1_);
               }
               invalidateSize();
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               this.clearTweens();
               _loc3_ = this._cards.length;
               _loc4_ = 0;
               _loc5_ = 0;
               _loc6_ = 0;
               while(_loc6_ < _loc3_)
               {
                  _loc1_ = this._cards[_loc6_];
                  _loc1_.updateSize(this._size);
                  _loc4_ = (HB_VEHICLE_CARD_PROPS.getWidth(this._size) + HB_VEHICLE_CARD_PROPS.getGap(this._size)) * _loc6_ + _loc5_;
                  if(_loc1_.isPickedState)
                  {
                     _loc5_ = HB_VEHICLE_CARD_PROPS.getWidthWide(this._size) - HB_VEHICLE_CARD_PROPS.getWidth(this._size);
                  }
                  if(this._hasAnim)
                  {
                     this._tweens.push(new Tween(TWEEN_DURATION,_loc1_,{"x":_loc4_}));
                  }
                  else
                  {
                     _loc1_.x = _loc4_;
                  }
                  _loc6_++;
               }
               this._hasAnim = false;
            }
         }
      }
      
      public function update(param1:Object) : void
      {
         if(this._data != param1)
         {
            this._data = Vector.<HBVehicleCardVO>(param1);
            invalidateData();
         }
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            invalidateSize();
         }
      }
      
      private function cleanCards() : void
      {
         var _loc1_:HBVehicleCard = null;
         for each(_loc1_ in this._cards)
         {
            removeChild(_loc1_);
            _loc1_.dispose();
         }
         this._cards.length = 0;
      }
      
      private function clearTweens() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens.length)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
            }
            this._tweens.splice(0,this._tweens.length);
         }
      }
      
      override public function get width() : Number
      {
         var _loc1_:uint = this._cards.length;
         if(_loc1_ > 0)
         {
            return HB_VEHICLE_CARD_PROPS.getWidth(this._size) * (_loc1_ - 1) + HB_VEHICLE_CARD_PROPS.getGap(this._size) * (_loc1_ - 1) + HB_VEHICLE_CARD_PROPS.getWidthWide(this._size);
         }
         return super.width;
      }
      
      private function onVehiclePickHandler(param1:HBVehicleCardEvent) : void
      {
         var _loc3_:HBVehicleCard = null;
         var _loc2_:int = param1.vehicleId;
         for each(_loc3_ in this._cards)
         {
            if(_loc3_.vehicleId != _loc2_ && !_loc3_.isDeadState)
            {
               _loc3_.state = HB_VEHICLE_CARD_STATE.DEFAULT;
            }
         }
         this._hasAnim = true;
         invalidateSize();
      }
   }
}
